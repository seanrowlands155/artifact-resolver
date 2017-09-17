
import org.sonatype.nexus.repository.storage.Component;
import org.sonatype.nexus.repository.storage.Query;
import org.sonatype.nexus.repository.storage.StorageFacet;

import groovy.json.JsonOutput;

def repo = repository.repositoryManager.get('maven-releases');
StorageFacet storageFacet = repo.facet(StorageFacet);
def tx = storageFacet.txSupplier().get();

tx.begin();

Iterable<Component> assets = tx.
        findComponents(Query.builder().where(\"version MATCHES '[0-9]{1,}.[0-9]{1,}.*-[A-Z]{3,}'\").build(), [repo]);
def urls = assets.collect {\"/repository/${repo.name}/${it.name()}/${it.version()}}\" };

tx.commit();
tx.close();

def result = JsonOutput.toJson([
        assets  : urls
]);
return result