async function fetchConversations() {
  const response = await fetch('/api/conversations');
  const result = await response.json();
  return result;
}

async function createConversations(user1, user2) {
  const response = await fetch('/api/conversations', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({user1, user2}),
  });
  if (response.status !== 201) {
    throw new Error('Failed to create conversation');
  }

  const result = await response.json();
  return result;
}

function getCookie(name) {
  if (validate(name)) return null;

  let cookieValue = null;
  const cookies = document.cookie.split(';');

  for (const rawCookie of cookies) {
    const cookie = rawCookie.trim();
    if (cookie.substring(0, name.length + 1) === (name + '=')) {
      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
      break;
    }
  }
  return cookieValue;

  function validate(name) {
    return !document.cookie || document.cookie === '' || !name;
  }
}
