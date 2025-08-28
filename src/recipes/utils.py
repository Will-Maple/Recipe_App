from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_graph():
  buffer = BytesIO()
  plt.savefig(buffer, format='png')
  buffer.seek(0)
  image_png=buffer.getvalue()
  graph=base64.b64encode(image_png)
  graph=graph.decode('utf-8')
  buffer.close()
  return graph

def get_chart(chart_type, data, **kwargs):
  plt.switch_backend('AGG')
  fig=plt.figure(figsize=(6,3))

  if chart_type == 'pie':
    plt.pie(data['sizes'], labels=data['labels'], autopct='%1.1f%%')
    plt.title('Recipes by Difficulty')
  elif chart_type == 'bar':
    plt.bar(data['labels'], data['counts'])
    plt.ylabel('Number of Recipes')
    plt.title('Recipes with/out optional values')
  elif chart_type == 'line':
    plt.plot(data['dates'], data['counts'], marker='o')
    plt.xticks(rotation=45)
    plt.ylabel('Recipes Created')
    plt.xlabel('Date')
    plt.title('When are Recipes created?')

  plt.tight_layout()
  graph = get_graph()
  plt.close()
  return graph