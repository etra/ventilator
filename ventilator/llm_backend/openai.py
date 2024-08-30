#openai llm implementation class
from ventilator.memory import MemoryItem
from ventilator.llm import LLM as LLMInterface
from openai import OpenAI


class LLM(LLMInterface):

    _client: OpenAI = None

    @property
    def client(self):
        if not self._client:
            self._client = OpenAI(api_key=self.app.config.OPENAI_API_KEY)
        return self._client

    def chat(self, conversation_id):
        #todo: convers messages json building to to_dict method
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": memory_item.role, "content": memory_item.content}
                for memory_item in self.app.memory.get(conversation_id)
            ]
        )
        self.app.log.info(response.choices[0].message)
        self.app.memory.add(conversation_id, MemoryItem(response.choices[0].message.role, response.choices[0].message.content))
        return response.choices[0].message.content

#
# #openai llm implementation class
# from ventilator.memory import MemoryItem
# from ventilator.llm import LLM as LLMInterface
# import json
# from openai import OpenAI
#
# tools = [
#     {
#         "type": "function",
#         "function": {
#             "name": "generate_random_words",
#             "description": "Generates random words as a source for the story to tell and if user provides word count we use it as parameter",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "word_count": {
#                         "type": "integer",
#                         "minimum": 1,
#                         "maximum": 100,
#                         "default": 10
#                     }
#                 }
#             }
#         }
#     }
# ]
#
#
# class LLM(LLMInterface):
#
#     _client: OpenAI = None
#
#     @property
#     def client(self):
#         if not self._client:
#             self._client = OpenAI(api_key=self.app.config.OPENAI_API_KEY)
#         return self._client
#
#     def chat(self, conversation_id):
#         self.app.memory.display(conversation_id)
#         #todo: convers messages json building to to_dict method
#         response = self.client.chat.completions.create(
#             model="gpt-4o",
#             messages=[
#                 {"role": memory_item.role, "content": memory_item.content}
#                 for memory_item in self.app.memory.get(conversation_id)
#             ],
#             tools=tools
#         )
#
#         if response.choices[0].finish_reason == "tool_calls":
#             tool_call = response.choices[0].message.tool_calls[0]
#             self.app.log.info(tool_call)
#             tool_id = tool_call.id
#             arguments = tool_call.function.arguments
#             function_name = tool_call.function.name
#             self.app.log.info(f"Function name: {function_name}")
#             self.app.log.info(f"Function arguments: {arguments}")
#             word_count = json.loads(arguments).get("word_count", 10)
#
#
#             answer_from_function = self.random_text_generator(word_count=word_count)
#
#             messages=[
#                 {"role": memory_item.role, "content": memory_item.content}
#                 for memory_item in self.app.memory.get(conversation_id)
#             ]
#
#             messages.append(response.choices[0].message)
#
#             messages.append(
#                 {
#                     "role": "tool",
#                     "content": json.dumps({"word_count": word_count, "random_words": answer_from_function}),
#                     "tool_call_id": tool_id
#                 }
#             )
#         # self.app.log.info(messages)
#
#         response = self.client.chat.completions.create(
#             model="gpt-4o",
#             messages=messages,
#             tools=tools
#         )
#         # self.app.log.info(response.choices[0].message)
#         self.app.memory.add(conversation_id, MemoryItem(response.choices[0].message.role, response.choices[0].message.content))
#
#         return response.choices[0].message.content
#
#
#     def random_text_generator(self, word_count=10):
#         import random
#         word_list = [
#             "data", "engineer", "pipeline", "ETL", "data warehouse", "data lake", "big data",
#             "batch processing", "streaming", "Kafka", "Apache Spark", "Flink", "Airflow", "workflow",
#             "data modeling", "SQL", "NoSQL", "data quality", "data governance", "cloud storage", "S3",
#             "data integration", "schema", "database", "sharding", "replication", "partitioning", "Hadoop",
#             "metadata", "data catalog", "data lineage", "real-time", "data ingestion", "data transformation",
#             "data validation", "data cleaning", "data orchestration", "serverless", "AWS", "Azure", "GCP",
#             "Snowflake", "Redshift", "BigQuery", "Delta Lake", "Iceberg", "Parquet", "ORC", "CSV",
#             "data architecture", "scalability", "performance optimization", "distributed systems", "microservices",
#             "containerization", "Kubernetes", "Docker", "CI/CD", "DevOps", "observability", "monitoring",
#             "logging", "metrics", "alerting", "fault tolerance", "data privacy", "security", "encryption",
#             "compression", "indexing", "data aggregation", "data analytics", "BI tools", "dashboard",
#             "data visualization", "machine learning", "AI", "predictive modeling", "feature engineering",
#             "data science", "Python", "R", "Java", "Scala", "API", "REST", "GraphQL", "JSON", "XML",
#             "data democratization", "data-driven", "business intelligence", "SQL queries", "data wrangling",
#             "data architecture", "data strategy", "data pipeline monitoring"
#         ]
#         random_text = ' '.join(random.choices(word_list, k=word_count))
#
#         return random_text
