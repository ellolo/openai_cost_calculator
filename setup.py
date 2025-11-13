from setuptools import setup, find_packages

setup(
    name="openai_cost_calculator_with_langchain",
    version="1.0.0",
    description="A library to estimate OpenAI API costs based on token usage, integrating with Langchain. This is a fork from v1.1.1 of openai_cost_calculator by Orkun Kınay and Murat Barkın Kınay (https://github.com/orkunkinay/openai_cost_calculator).",
    author="Marco Pennacchiotti (forked from openai_cost_calculator by Orkun Kınay and Murat Barkın Kınay)",
    packages=find_packages(),
    include_package_data=True, 
    package_data={
        "openai_cost_calculator": ["data/gpt_pricing_data.csv"],
    },
    python_requires='>=3.8.1',
)
