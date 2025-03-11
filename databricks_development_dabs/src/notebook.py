# Databricks notebook source
# MAGIC %md
# MAGIC # Default notebook
# MAGIC
# MAGIC This default notebook is executed using Databricks Workflows as defined in resources/databricks_development_dabs.job.yml.

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# MAGIC %sh
# MAGIC pip list

# COMMAND ----------

from databricks_development_dabs import main

main.get_taxis(spark).show(10)
