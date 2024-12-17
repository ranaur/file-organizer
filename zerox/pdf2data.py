import sys
from pyzerox import zerox
from pathlib import Path
import os
import json
import asyncio

### Model Setup (Use only Vision Models) Refer: https://docs.litellm.ai/docs/providers ###

## placeholder for additional model kwargs which might be required for some models
kwargs = {}

## system prompt to use for the vision model
custom_system_prompt = None

try:
    prompt_file = os.environ["ZEROX_PROMPT_FILE"]
    custom_system_prompt = Path(prompt_file).read_text()
except KeyError:
    print("Using default prompt")

# to override

model = os.environ["ZEROX_MODEL"]

# Define main async entrypoint
async def main():
    file_path=sys.argv[1]

    ## process only some pages or all
    select_pages = None ## None for all, but could be int or list(int) page numbers (1 indexed)

    output_dir = "./output_test" ## directory to save the consolidated markdown file
    result = await zerox(file_path=file_path, model=model, output_dir=output_dir,
                        custom_system_prompt=custom_system_prompt,select_pages=select_pages, **kwargs)
    return result


# run the main function:
result = asyncio.run(main())

# print markdown result
#print(result)

print(result.pages[0].content)
