
# BASE
LIST = {'get':'list'}

CREATE = {'post':'create'}

RETRIEVE = {'get':'retrieve'}

UPDATE = {'put':'update'}

PARTIAL_UPDATE = {'patch':'partial_update'}

DESTROY = {'delete':'destroy'}


# MULTIPLE 
LIST_CREATE = {**LIST, **CREATE}

RETRIEVE_UPDATE = {**RETRIEVE, **UPDATE, **PARTIAL_UPDATE}

RETRIEVE_DESTROY = {**RETRIEVE, **DESTROY}

RETRIEVE_UPDATE_DESTROY = {**RETRIEVE, **UPDATE, **PARTIAL_UPDATE, **DESTROY}

