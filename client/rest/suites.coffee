class SuitesApi
  append: (suite, { onSuccess, onError }) =>
    request = $.get
      url: '/suites/append'
      data: suite
    request.done (suitId) =>
      if suitId.id?
        _.extend suite, { id: suitId.id }
        onSuccess { suite }
      else
        onError 'Server does not return valid id.'
    request.fail (err) => onError { message: err.responseText }

  list: ({ onSuccess, onError }) =>
    request = $.get { url: '/suites/list' }
    request.done (suitesList) => onSuccess suitesList
    request.fail (err) => onError { message: err.responseText }

  update: (suite, { command }, { onSuccess, onError }) =>
    request = $.post
      url: "/suites/update"
      data:  JSON.stringify { id: suite.id, cmd: command }
      dataType: 'json'
    request.done (status) => onSuccess { }
    request.fail (err) => onError { message: err.responseText }

export default new SuitesApi
