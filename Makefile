MD = $(wildcard *.md)

.PHONY: clean

all: gimli

gimli: $(MD)
	@mkdir -p ./pdf/
	@$(foreach x,$(MD:.md=), \
		echo "Baking $(x)"; \
		gimli $(x).md; \
	)
	@mv *.pdf ./pdf/;

clean:
	@git clean -xfd
