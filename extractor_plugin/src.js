const extractUtlaUkGovspeak = () => {
  const res = {
    meta: {},
    data: {}
  }
  document
    .querySelectorAll('.govspeak')
    .forEach(el => {
      const table = el.querySelector('table')
      if (table) {
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
        const rows = table.querySelectorAll('tr')
        console.info('Entries found: ' + rows.length)

        let i = 0, sum = 0
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

const extractUtlaDashboard = () => {
  const res = {
    meta: {},
    data: {}
  }
  let i = 0, sum = 0
  document
    .querySelector('.feature-list')
    .querySelectorAll('span.feature-list-item')
    .forEach(el => {
      const [region, value] = el.textContent.split(':')
      const cur = parseInt(value.replace(',', ''))
      res.data[region.trim()] = cur
      sum += cur
      i++
    })
  res.meta.total = sum
  res.meta.entries = i

  const descriptionRaw = document.querySelector('div#ember16') // happens to be a title
  if (descriptionRaw) {
    const descriptionText = descriptionRaw.textContent.trim()
    const dateRegex = /\d+\w{2}\s\w+\s\d{4}/g
    const maybeDate = descriptionText.match(dateRegex)
    res.meta.date = maybeDate ? maybeDate[0] : undefined
    res.meta.description = descriptionText
  }
  return JSON.stringify(res, undefined, 2)
}

const LegacyUtlaCasesPage = 'https://www.gov.uk/government/publications/coronavirus-covid-19-number-of-cases-in-england/coronavirus-covid-19-number-of-cases-in-england'
const UkCasesDashboard = 'https://www.arcgis.com/apps/opsdashboard/index.html#/f94c3c90da5b4e9f9a0b19484dd4bb14'

chrome.runtime.onMessage.addListener(request => {
  if (request.message === 'clicked_browser_action') {
    const urlIs = (expected) => request.url.indexOf(expected) !== -1

    let jsonRes
    if (urlIs(LegacyUtlaCasesPage)) {
      jsonRes = extractUtlaUkGovspeak()
    } else if (urlIs(UkCasesDashboard)) {
      jsonRes = extractUtlaDashboard()
    }

    if (jsonRes) {
      document.querySelector('body').innerHTML = jsonRes
    } else {
      console.warn('No data has been extracted')
    }
  }
})
