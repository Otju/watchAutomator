export const post = (parts) => {
  const host = window.location.hostname
  const url = `http://${host}:5000/${parts.join('/')}`
  fetch(url, { method: 'POST' })
}

export const get = async (page) => {
  const host = window.location.hostname
  const url = `http://${host}:5000/${page}`
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
    },
  })
  const data = await response.json()
  console.log(data)
  return data
}
