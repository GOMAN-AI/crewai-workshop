import asyncio
from aioconsole import ainput
from joke_teller.crew import CreateJokeCrew
from shared.tracing import traceable

@traceable
async def main():
    while True:
        channel = await ainput("Enter an youtube channel handle (format: @exampleChannel): ")

        if channel.startswith('@'):
            break
        print("Error: Channel handle must start with '@'. Please try again.")

        crew = CreateJokeCrew().crew()
        inputs = { "channel": channel }
        await crew.kickoff_async(inputs=inputs)

if __name__ == '__main__':
    asyncio.run(main())
