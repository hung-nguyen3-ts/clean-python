import json

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer, TopicPartition
from aiokafka.helpers import create_ssl_context


class CustomKafkaProducer(AIOKafkaProducer):
    topic_name: str
    topic_num_partitions: int
    topic_replication_factor: int

    @staticmethod
    async def get_kafka_producer(
        bootstrap_servers_url: str,
        topic_name: str,
        client_id: str,
        acks: str,
        batch_size: int,
        topic_num_partitions: int,
        topic_replication_factor: int,
        enable_authentication_methods: bool,
        sasl_mechanism: str,
        sasl_plain_username: str,
        sasl_plain_password: str,
        security_protocol: str,
        ssl_ca_file_path: str,
    ):
        config_dict = {
            "bootstrap_servers": bootstrap_servers_url,
            "client_id": client_id,
            # "acks": acks,
            "max_batch_size": batch_size,
            "value_serializer": lambda d: json.dumps(d).encode("ascii"),
        }
        if enable_authentication_methods:
            ssl_context = create_ssl_context(cafile=ssl_ca_file_path)
            config_dict = config_dict | {
                "sasl_mechanism": sasl_mechanism,
                "sasl_plain_username": sasl_plain_username,
                "sasl_plain_password": sasl_plain_password,
                "security_protocol": security_protocol,
                "ssl_context": ssl_context,
            }

        custom_producer = CustomKafkaProducer(**config_dict)
        custom_producer.topic_name = topic_name
        custom_producer.topic_num_partitions = topic_num_partitions
        custom_producer.topic_replication_factor = topic_replication_factor
        await custom_producer.start()
        return custom_producer


class CustomKafkaConsumer(AIOKafkaConsumer):
    topic_name: str
    partitions: list[TopicPartition]

    @staticmethod
    async def get_kafka_consumer(
        bootstrap_servers_url: str,
        topic_name: str,
        client_id: str,
        group_id: str,
        retry_backoff_ms: int,
        auto_offset_reset: str,
        enable_auto_commit: bool,
        enable_authentication_methods: bool,
        sasl_mechanism: str,
        sasl_plain_username: str,
        sasl_plain_password: str,
        security_protocol: str,
        ssl_ca_file_path: str,
    ):
        config_dict = {
            "bootstrap_servers": bootstrap_servers_url,
            "client_id": client_id,
            "group_id": group_id,
            # "retry_backoff_ms": retry_backoff_ms,
            "enable_auto_commit": enable_auto_commit,
            "auto_offset_reset": auto_offset_reset,
            "value_deserializer": lambda d: json.loads(d.decode("ascii")),
        }
        if enable_authentication_methods:
            ssl_context = create_ssl_context(cafile=ssl_ca_file_path)
            config_dict = config_dict | {
                "sasl_mechanism": sasl_mechanism,
                "sasl_plain_username": sasl_plain_username,
                "sasl_plain_password": sasl_plain_password,
                "security_protocol": security_protocol,
                "ssl_context": ssl_context,
            }

        custom_consumer = CustomKafkaConsumer(
            topic_name,
            **config_dict,
        )
        custom_consumer.topic_name = topic_name
        paritions_set = custom_consumer.partitions_for_topic(topic_name)

        custom_consumer.partitions = []
        if paritions_set is not None:
            custom_consumer.partitions = [
                TopicPartition(topic_name, partition) for partition in paritions_set
            ]
        await custom_consumer.start()
        return custom_consumer
