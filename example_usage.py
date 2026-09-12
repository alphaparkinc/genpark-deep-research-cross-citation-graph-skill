from client import DeepResearchCrossCitationGraphClient

def main():
    client = DeepResearchCrossCitationGraphClient()
    res = client.build_citation_graph()
    print('Cross Citation Graph: ' + res['graph_id'] + ' (' + res['research_topic'] + ')')
    print('Nodes: ' + str(res['nodes_count']) + ' | Edges: ' + str(res['citation_edges_count']) + ' | Authority: ' + str(res['authority_weighted_score']))
    print('Circular References: ' + str(res['circular_references_detected']) + ' | Primary Node: ' + res['primary_consensus_node'])
    print('Telemetry URL: ' + res['graph_telemetry_url'])

if __name__ == '__main__':
    main()
