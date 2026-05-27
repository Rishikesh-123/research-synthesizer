import streamlit as st
from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

#Load API KEy
load_dotenv

#We need to push something today also