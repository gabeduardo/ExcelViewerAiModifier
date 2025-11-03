from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

system_template = """
You are an AI underwriter in fleet that enriches Excel data.
Here is the JSON rule set:
{rules_json}

Here is the current sheet data:
{sheet_data}

Apply the rules and return the updated rows as JSON.
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(template="Ready to enrich.")

chat_prompt_template = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])