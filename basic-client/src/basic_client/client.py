from parlant.client import ParlantClient

client = ParlantClient(base_url="http://localhost:8800")

# Create an agent following https://www.parlant.io/docs/tutorial/building-the-skeleton/setup-your-agent
AGENT_ID="EI6HZQWAe1"
agent = client.agents.retrieve(AGENT_ID)

CUSTOMER_ID="CkHAYIsGpB"
customer = client.customers.retrieve(CUSTOMER_ID)

session = client.sessions.create(
    agent_id=AGENT_ID, 
    customer_id=CUSTOMER_ID,
    allow_greeting=False)

VARIABLE_ID="o6TBtjD5Kx"
variable = client.variables.retrieve(VARIABLE_ID)
TAG_ID="4MV2dAy-88"
tag = client.tags.retrieve(TAG_ID)

while True:
    customer_message = input("Customer: ")

    if customer_message in ("quit", "bye", "exit", "cya l8r m8"):
        break

    customer_event = client.sessions.create_event(
        session_id=session.id,
        source="customer",
        kind="message",
        message=customer_message,
    )

    agent_event, *_ = client.sessions.list_events(
        session_id=session.id,
        source="ai_agent",
        kinds="message",
        min_offset=customer_event.offset,
    )

    # Let type-checker know we do have data here
    assert agent_event.data
    agent_message = agent_event.data["message"]

    print(f"{agent.name}: {agent_message}")
