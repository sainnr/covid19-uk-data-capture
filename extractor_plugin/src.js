chrome.runtime.onMessage.addListener(request => {
  if (request.message === 'clicked_browser_action') {
    const query = '.govspeak'
    const elements = document.querySelectorAll(query)
    const res = {}
    elements.forEach(el => {
      const tab = el.querySelector('table')
      if (tab) {
        const rows = tab.querySelectorAll('tr')
        console.log('Entries found: ' + rows.length)
        let i = 0 // to skip the first row
        rows.forEach(row => {
          const k = row.children[0].textContent
          const v = row.children[1].textContent
          if (i) {
            res[k] = parseInt(v)
          }
          i++
        })
      }
    })
    const jsonRes = JSON.stringify(res, undefined, 2)
    document.querySelector('body').innerHTML = jsonRes
  }
})
