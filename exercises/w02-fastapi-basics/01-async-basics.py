import asyncio

async def asycn_process_data(data:str) -> str:
    await asyncio.sleep(1)
    return f"处理完成：{data}"

async def async_process_multiple():
    # 创建多个任务
    task1 = asycn_process_data("数据1")
    task2 = asycn_process_data("数据2") 
    task3 = asycn_process_data("数据3")

    # 并发执行
    result1, result2, result3 = await asyncio.gather(task1, task2, task3)
    return [result1, result2, result3]

import time

start = time.time()
results = asyncio.run(async_process_multiple())
end = time.time()

print(f"结果：{results}")
print(f"耗时：{end - start:.1f}秒")