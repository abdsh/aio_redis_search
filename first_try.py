import aioredis
import asyncio
import uvloop

uvloop.install()

async def main():
    
    redis = aioredis.from_url("redis://localhost")

    async def test_query():
        response = await redis.execute_command(
            'FT.SEARCH', 'books-idx', "@categories:{Fantasy}",
            'RETURN', '1', 'title'   
        )

        return response


    result = await test_query()

    for i in range(2,len(result),2):
        print(result[i])
    
asyncio.run(main()) 