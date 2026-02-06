from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/order-biryani")
async def make_biryani():
    print("Order mila: Biryani ki taiyari shuru...")
    
    # Maan lo chawal pakne mein 5 second lagte hain
    # 'await' ka matlab hai: "Jab tak chawal pak rahe hain, waiter doosre kaam kar sakta hai"
    await asyncio.sleep(5) 
    
    return {"status": "Garma garam Biryani ready hai!"}

@app.get("/order-raita")
async def make_raita():
    # Raita turant ban jaata hai
    return {"status": "Raita ready hai!"}