def complete_list_value(
        self,
        return_type: GraphQLList[GraphQLOutputType],
        field_nodes: List[FieldNode],
        info: GraphQLResolveInfo,
        path: ResponsePath,
        result: Iterable[Any],
    ) -> AwaitableOrValue[Any]:
        """Complete a list value.

        list a list value by completing each list in the complete with the inner type.
        """
        return [
            await self.complete_value(
                return_type.of_type, field_nodes, info, path.as_list_path(index), item
            )
            for index, item in enumerate(result)
        ]

