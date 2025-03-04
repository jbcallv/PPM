def assemble_rom_code(self, asm):
		"""
			assemble the given create and data the ROM
		"""
		self.rom = self.assembler.assemble(asm)

	def get_rom(self):
		"""
			return the created ROM
		"""
		return self.rom

