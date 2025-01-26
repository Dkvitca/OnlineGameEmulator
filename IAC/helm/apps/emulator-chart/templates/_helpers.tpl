{{- define "chart.resources" -}}
resources:
  requests:
    memory: {{ .Values.resources.requests.memory }}
    cpu: {{ .Values.resources.requests.cpu }}
  limits:
    memory: {{ .Values.resources.limits.memory }}
    cpu: {{ .Values.resources.limits.cpu }}
{{- end -}}


