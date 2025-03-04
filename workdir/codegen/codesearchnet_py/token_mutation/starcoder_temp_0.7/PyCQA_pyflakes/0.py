def checkDeadScopes(self):
        """
        those at look which have been fully examined and report those in them
        which were imported but unused.
        """
        for scope in self.scopes.values():
            if scope.dead:
                self.deadScopes.append(scope)

    def _checkUnusedImports(self):
        """
        Check for any unused imports.

        This checks for any imports that are not used, as well as any
        imports of unused modules.
        """
        # usedModules is a set of modules imported, whether or not they are
        # actually used.
        usedModules = set()

        # usedImports is a set of imports that are used.  If we find that an
        # import is used, we remove it from this set.  If there are no
        # imports left in this set at the end of the check, we're done.
        usedImports = set()

        for scope in self.scopes.values():
            if scope.imports:
                for imp in scope.imports:
                    usedModules.add(imp.module)
                    if imp.name not in scope.used:
                        self.unusedImports.append((imp, scope))
                    else:
                        usedImports.add(imp)

        for scope in self.scopes.values():
            if scope.imports:
                for imp in scope.imports:
                    if imp not in usedImports:
                        self.unusedImports.append((imp, scope))

        # Now see if any of the modules we imported are unused.
        for module, importList in self.importedModules.items():
            if module not in usedModules and module not in self.hiddenImports:
                # If this is a wildcard import, we don't really care.
                if any([x[0] == "*" for x in importList]):
                    continue
                for imp, scope in self.unusedImports:
                    if imp.module == module:
                        self.unusedImports.append((imp, scope))
                        break


