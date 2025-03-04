def import_intermediate_throw_event_to_graph(diagram_graph, process_id, process_attributes, element):
        """
        Adds to graph the new element that represents BPMN intermediate throw event.
        Intermediate throw event inherits sequence of eventDefinitionRef from Event type.
        Separate methods for each id type are required since each of them has different variants
        (Message, Error, Signal etc.).

        :param diagram_graph: NetworkX graph representing a xml process diagram,
        :param process_id: string object, representing an ID of process element,
        :param process_attributes: dictionary that holds attribute values of 'process' element, which is event of
           imported flow node,
        :param element: object representing a BPMN XML 'intermediateThrowEvent' element.
        """

        intermediate_throw_event = diagram_graph.node[element.get('id')]
        intermediate_throw_event['type'] = 'intermediateThrowEvent'
        intermediate_throw_event['process_id'] = process_id
        intermediate_throw_event['process_name'] = process_attributes.get('name')
        intermediate_throw_event['process_documentation'] = process_attributes.get('documentation')
        intermediate_throw_event['eventDefinitionRef'] = [element.get('eventDefinitionRef')]

