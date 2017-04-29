class RunsApi
  list: ({ onSuccess, onError }) =>
    request = $.get { url: '/runs/list' }
    request.done (suitesList) => onSuccess suitesList
    request.fail (err) => onError { message: err.responseText }

export default new RunsApi
