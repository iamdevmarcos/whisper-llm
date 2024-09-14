from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

import pandas as pd

df = pd.read_csv('df_rent.csv')

agent = create_pandas_dataframe_agent(
  ChatOpenAI(model='gpt-3.5-turbo'),
  df,
  verbose=True,
  agent_type=AgentType.OPENAI_FUNCTIONS
)

agent.invoke("")