async function fetchConversations() {
  const response = await fetch('/api/conversations');
  const result = await response.json();
  return result;
}

async function createConversations(user1, user2) {
  const response = await fetch('/api/conversations', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({user1, user2}),
  });
  if (response.status !== 201) {
    throw new Error('Failed to create conversation');
  }

  const result = await response.json();
  return result;
}
