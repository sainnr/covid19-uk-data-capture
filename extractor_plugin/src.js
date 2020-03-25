const extractUtlaUkGovspeak = () => {
  const res = {
    meta: {},
    data: {}
  }
  const query = '.govspeak'
  const elements = document.querySelectorAll(query)
  elements.forEach(el => {
    const paragraphs = el.querySelectorAll('p')
    if (paragraphs) {
      res.meta.description = paragraphs.item(0).textContent
      const dateTimeRaw = paragraphs.item(2)
      if (dateTimeRaw) {
        const dateTimeRegex = /(\d:\d*am|\d+ \w+ \d+)/g
        const [time, date] = dateTimeRaw.textContent.match(dateTimeRegex)
        res.meta.date = date
        res.meta.time = time
      }
    }
    const table = el.querySelector('table')
    if (table) {
      const rows = table.querySelectorAll('tr')
      console.info('Entries found: ' + rows.length)

      let sum = 0
      let i = 0 // to skip the first row
      rows.forEach(row => {
        const k = row.children[0].textContent
        const v = row.children[1].textContent
        if (i) {
          const cur = parseInt(v)
          res.data[k] = cur
          sum += cur
        }
        i++
      })
      res.meta.total = sum
      res.meta.entries = i
    }
  })
  return JSON.stringify(res, undefined, 2)
}

const LegacyUtlaCasesPage = 'https://www.gov.uk/government/publications/coronavirus-covid-19-number-of-cases-in-england/coronavirus-covid-19-number-of-cases-in-england'

chrome.runtime.onMessage.addListener(request => {
  if (request.message === 'clicked_browser_action') {
    const urlIs = (expected) => request.url.indexOf(expected) !== -1

    let jsonRes
    if (urlIs(LegacyUtlaCasesPage)) {
      jsonRes = extractUtlaUkGovspeak()
    }

    if (jsonRes) {
      document.querySelector('body').innerHTML = jsonRes
    } else {
      console.warn('No data has been extracted')
    }
  }
})
