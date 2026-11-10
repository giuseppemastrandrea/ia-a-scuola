# iNaturalist API v1: gli endpoint per osservazioni e specie

Estratto dalla specifica ufficiale (https://api.inaturalist.org/v1/swagger.json, versione 1.3.0), scaricata il 10/11/2026. Documentazione completa: https://api.inaturalist.org/v1/docs/

## Note generali dalla documentazione

# https://api.inaturalist.org/v1/

[iNaturalist](https://www.inaturalist.org/) is a global community of
naturalists, scientists, and members of the public sharing over a million
wildlife sightings to teach one another about the natural world while
creating high quality citizen science data for science and conservation.

These API methods return data in JSON/JSONP and PNG response formats. They
are meant to supplement the existing [iNaturalist
API](https://www.inaturalist.org/pages/api+reference), implemented in Ruby
on Rails, which has more functionality and supports more write operations,
but tends to be slower and have less consistent response formats. Visit our
[developers page](https://www.inaturalist.org/pages/developers) for more
information. Write operations that expect and return JSON describe a single
`body` parameter that represents the request body, which should be specified
as JSON. See the "Model" of each body parameter for attributes that we
accept in these JSON objects.

Multiple values for a single URL parameter should be separated by commas,
e.g. `taxon_id=1,2,3`.

Map tiles are generated using the
[node-mapnik](https://github.com/mapnik/node-mapnik) library, following the
XYZ map tiling scheme. The "Observation Tile" methods accept nearly all the
parameters of the observation search APIs, and will generate map tiles
reflecting the same observations returned by searches. These
"Observation Tile" methods have corresponding
[UTFGrid](https://github.com/mapbox/utfgrid-spec) JSON
responses which return information needed to make interactive maps.

Authentication in the Node API is handled via JSON Web Tokens (JWT). To
obtain one, make an [OAuth-authenticated
request](http://www.inaturalist.org/pages/api+reference#auth) to
https://www.inaturalist.org/users/api_token. Each JWT will expire after 24
hours. Authentication required for all PUT and POST requests. Some GET
requests will also include private information like hidden coordinates if
the authenticated user has permission to view them.

Photos served from https://static.inaturalist.org and
https://inaturalist-open-data.s3.amazonaws.com have multiple size
variants and not all size variants are returned in responses. To access
other sizes, the photo URL can be modified to replace only the size
qualifier (each variant shares the exact same extension). The domain a photo
is hosted under reflects the license under which the photo is being shared,
and the domain may change over time if the license changes. Photos in
the `inaturalist-open-data` domain are shared under open licenses. These can
be accessed in bulk in the [iNaturalist AWS Open Dataset](
https://registry.opendata.aws/inaturalist-open-data/). Photos in the
`static.inaturalist.org` domain do not have open licenses.

The available photo sizes are:
* original (max 2048px in either dimension)
* large (max 1024px in either dimension)
* medium (max 500px in either dimension)
* small (max 240px in either dimension)
* thumb (max 100px in either dimension)
* square (75px square)

iNaturalist Website: https://www.inaturalist.org/

Open Source Software: https://github.com/inaturalist/

## Terms of Use

Use of this API is subject to the iNaturalist
[Terms of Service](https://www.inaturalist.org/terms) and
[Privacy Policy](https://www.inaturalist.org/privacy). We will block any
use of our API that violates our Terms or Privacy Policy without notice.
The API is intended to support application development, not data scraping.
For pre- generated data exports, see
https://www.inaturalist.org/pages/developers.

Please note that we throttle API usage to a max of 100 requests per minute,
though we ask that you try to keep it to 60 requests per minute or lower,
and to keep under 10,000 requests per day. If we notice usage that has
serious impact on our performance we may institute blocks without
notification.

Terms of Service: https://www.inaturalist.org/terms

Privacy Policy: https://www.inaturalist.org/privacy

## GET https://api.inaturalist.org/v1/observations

Observation Search

Given zero to many of following parameters, returns observations
matching the search criteria. The large size of the observations index
prevents us from supporting the `page` parameter when retrieving records
from large result sets. If you need to retrieve large numbers of
records, use the `per_page` and `id_above` or `id_below` parameters
instead.

| Parametro | Tipo | Descrizione |
|---|---|---|
| `acc` | boolean | Whether or not positional accuracy / coordinate uncertainty has been specified |
| `captive` | boolean | Captive or cultivated observations |
| `endemic` | boolean | Observations whose taxa are endemic to their location |
| `geo` | boolean | Observations that are georeferenced |
| `id_please` | boolean | Observations with the deprecated `ID, Please!` flag. Note that this will return observations, but that this attribute is no longer used. |
| `identified` | boolean | Observations that have community identifications |
| `introduced` | boolean | Observations whose taxa are introduced in their location |
| `mappable` | boolean | Observations that show on map tiles |
| `native` | boolean | Observations whose taxa are native to their location |
| `out_of_range` | boolean | Observations whose taxa are outside their known ranges |
| `pcid` | boolean | Observations identified by the curator of a project. If the `project_id` parameter is also specified, this will only consider observations identified by curators of the specified project(s) |
| `photos` | boolean | Observations with photos |
| `popular` | boolean | Observations that have been favorited by at least one user |
| `sounds` | boolean | Observations with sounds |
| `taxon_is_active` | boolean | Observations of active taxon concepts |
| `threatened` | boolean | Observations whose taxa are threatened in their location |
| `verifiable` | boolean | Observations with a `quality_grade` of either `needs_id` or `research`. Equivalent to `quality_grade=needs_id,research` |
| `licensed` | boolean | License attribute of an observation must not be null |
| `photo_licensed` | boolean | License attribute of at least one photo of an observation must not be null |
| `expected_nearby` | boolean | Observation taxon is expected nearby |
| `id` | array di string | Must have this ID |
| `not_id` | array di string | Must not have this ID |
| `license` | array di string | Observation must have this license Valori: cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa, cc0. |
| `ofv_datatype` | array di string | Must have an observation field value with this datatype |
| `photo_license` | array di string | Must have at least one photo with this license Valori: cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa, cc0. |
| `place_id` | array di integer | Must be observed within the place with this ID |
| `project_id` | array di string | Must be added to the project this ID or slug |
| `rank` | array di string | Taxon must have this rank Valori: stateofmatter, kingdom, phylum, subphylum, superclass, class, subclass, superorder, order, suborder, infraorder, superfamily, epifamily, family, subfamily, supertribe, tribe, subtribe, genus, genushybrid, species, hybrid, subspecies, variety, form. |
| `site_id` | array di string | Must be affiliated with the iNaturalist network website with this ID |
| `sound_license` | array di string | Must have at least one sound with this license Valori: cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa, cc0. |
| `taxon_id` | array di string | Only show observations of these taxa and their descendants |
| `without_taxon_id` | array di string | Exclude observations of these taxa and their descendants |
| `taxon_name` | array di string | Taxon must have a scientific or common name matching this string |
| `user_id` | array di string | User must have this ID or login |
| `user_login` | array di string | User must have this login |
| `ident_user_id` | integer | Observations identified by a particular user |
| `hour` | array di string | Must be observed within this hour of the day |
| `day` | array di string | Must be observed within this day of the month |
| `month` | array di string | Must be observed within this month |
| `year` | array di string | Must be observed within this year |
| `created_day` | array di string | Must be created within this day of the month |
| `created_month` | array di string | Must be created within this month |
| `created_year` | array di string | Must be created within this year |
| `term_id` | array di integer | Must have an annotation using this controlled term ID |
| `term_value_id` | array di integer | Must have an annotation using this controlled value ID. Must be combined with the `term_id` parameter |
| `without_term_id` | integer | Exclude observations with annotations using this controlled value ID. |
| `without_term_value_id` | array di integer | Exclude observations with annotations using this controlled value ID. Must be combined with the `term_id` parameter |
| `term_id_or_unknown` | array di integer | Must be combined with the `term_value_id` or the `without_term_value_id` parameter. Must have an annotation using this controlled term ID and associated term value IDs or be missing this annotation. |
| `annotation_user_id` | array di string | Must have an annotation created by this user |
| `acc_above` | string | Must have a positional accuracy above this value (meters) |
| `acc_below` | string | Must have a positional accuracy below this value (meters) |
| `acc_below_or_unknown` | string | Positional accuracy must be below this value (in meters) or be unknown |
| `d1` | string | Must be observed on or after this date |
| `d2` | string | Must be observed on or before this date |
| `created_d1` | string | Must be created at or after this time |
| `created_d2` | string | Must be created at or before this time |
| `created_on` | string | Must be created on this date |
| `observed_on` | string | Must be observed on this date |
| `unobserved_by_user_id` | integer | Must not be of a taxon previously observed by this user |
| `apply_project_rules_for` | string | Must match the rules of the project with this ID or slug |
| `cs` | string | Taxon must have this conservation status code. If the `place_id` parameter is also specified, this will only consider statuses specific to that place |
| `csa` | string | Taxon must have a conservation status from this authority. If the `place_id` parameter is also specified, this will only consider statuses specific to that place |
| `csi` | array di string | Taxon must have this IUCN conservation status. If the `place_id` parameter is also specified, this will only consider statuses specific to that place Valori: LC, NT, VU, EN, CR, EW, EX. |
| `geoprivacy` | array di string | Must have this geoprivacy setting Valori: obscured, obscured_private, open, private. |
| `taxon_geoprivacy` | array di string | Filter observations by the most conservative geoprivacy applied by a conservation status associated with one of the taxa proposed in the current identifications. Valori: obscured, obscured_private, open, private. |
| `obscuration` | array di string | Must have `geoprivacy` or `taxon_geoprivacy` fields matching these values Valori: obscured, private, none. |
| `hrank` | string | Taxon must have this rank or lower Valori: stateofmatter, kingdom, phylum, subphylum, superclass, class, subclass, superorder, order, suborder, infraorder, superfamily, epifamily, family, subfamily, supertribe, tribe, subtribe, genus, genushybrid, species, hybrid, subspecies, variety, form. |
| `lrank` | string | Taxon must have this rank or higher Valori: stateofmatter, kingdom, phylum, subphylum, superclass, class, subclass, superorder, order, suborder, infraorder, superfamily, epifamily, family, subfamily, supertribe, tribe, subtribe, genus, genushybrid, species, hybrid, subspecies, variety, form. |
| `iconic_taxa` | array di string | Taxon must by within this iconic taxon Valori: Actinopterygii, Animalia, Amphibia, Arachnida, Aves, Chromista, Fungi, Insecta, Mammalia, Mollusca, Reptilia, Plantae, Protozoa, unknown. |
| `id_above` | string | Must have an ID above this value |
| `id_below` | string | Must have an ID below this value |
| `identifications` | string | Identifications must meet these criteria Valori: most_agree, most_disagree, some_agree. |
| `lat` | number | Must be within a {`radius`} kilometer circle around this lat/lng (*lat, *lng, radius) |
| `lng` | number | Must be within a {`radius`} kilometer circle around this lat/lng (*lat, *lng, radius) |
| `radius` | string | Must be within a {`radius`} kilometer circle around this lat/lng (*lat, *lng, radius) |
| `nelat` | number | Must be within this bounding box (*nelat, *nelng, *swlat, *swlng) |
| `nelng` | number | Must be within this bounding box (*nelat, *nelng, *swlat, *swlng) |
| `swlat` | number | Must be within this bounding box (*nelat, *nelng, *swlat, *swlng) |
| `swlng` | number | Must be within this bounding box (*nelat, *nelng, *swlat, *swlng) |
| `list_id` | integer | Taxon must be in the list with this ID |
| `not_in_project` | string | Must not be in the project with this ID or slug |
| `not_matching_project_rules_for` | string | Must not match the rules of the project with this ID or slug |
| `observation_accuracy_experiment_id` | array di integer | Must included in this observation accuracy experiment |
| `fails_dqa_accurate` | boolean | Must be voted as not accurately depicting an organism or scene |
| `fails_dqa_date` | boolean | Must be voted as not having an accurate date |
| `fails_dqa_evidence` | boolean | Must be voted as not evidence of an organism |
| `fails_dqa_location` | boolean | Must be voted as not having an accurate location |
| `fails_dqa_needs_id` | boolean | Must be voted as the community ID cannot be improved |
| `fails_dqa_recent` | boolean | Must be voted as not recent evidence of an organism |
| `fails_dqa_subject` | boolean | Must be voted as not having evidence related to a single subject |
| `fails_dqa_wild` | boolean | Must be voted as not wild |
| `q` | string | Search observation properties. Can be combined with `search_on` |
| `search_on` | string | Properties to search on, when combined with `q`. Searches across all properties by default Valori: names, tags, description, place. |
| `quality_grade` | string | Must have this quality grade Valori: casual, needs_id, research. |
| `updated_since` | string | Must be updated since this time |
| `viewer_id` | string | See `reviewed` |
| `reviewed` | boolean | Observations have been reviewed by the user with ID equal to the value of the `viewer_id` parameter |
| `locale` | string | Locale preference for taxon common names |
| `preferred_place_id` | integer | Place preference for regional taxon common names |
| `ttl` | string | Set the `Cache-Control` HTTP header with this value as `max-age`, in seconds. This means subsequent identical requests will be cached on iNaturalist servers, and commonly within web browsers |
| `page` | string | Pagination `page` number |
| `per_page` | string | Number of results to return in a `page`. The maximum value is generally 200 unless otherwise noted |
| `order` | string | Sort order Valori: desc, asc. Predefinito: desc. |
| `order_by` | string | Sort field Valori: created_at, geo_score, id, observed_on, random, species_guess, updated_at, votes. Predefinito: created_at. |
| `only_id` | boolean | Return only the record IDs |

## GET https://api.inaturalist.org/v1/observations/species_counts

Observation Species Counts

Given zero to many of following parameters, returns `leaf taxa`
associated with observations matching the search criteria and the count of
observations they are associated with, ordered by count descending.
`Leaf taxa` are the leaves of the taxonomic tree containing only the
taxa associated with observations matching the search criteria.

| Parametro | Tipo | Descrizione |
|---|---|---|
| `acc` | boolean | Whether or not positional accuracy / coordinate uncertainty has been specified |
| `captive` | boolean | Captive or cultivated observations |
| `endemic` | boolean | Observations whose taxa are endemic to their location |
| `geo` | boolean | Observations that are georeferenced |
| `id_please` | boolean | Observations with the deprecated `ID, Please!` flag. Note that this will return observations, but that this attribute is no longer used. |
| `identified` | boolean | Observations that have community identifications |
| `introduced` | boolean | Observations whose taxa are introduced in their location |
| `mappable` | boolean | Observations that show on map tiles |
| `native` | boolean | Observations whose taxa are native to their location |
| `out_of_range` | boolean | Observations whose taxa are outside their known ranges |
| `pcid` | boolean | Observations identified by the curator of a project. If the `project_id` parameter is also specified, this will only consider observations identified by curators of the specified project(s) |
| `photos` | boolean | Observations with photos |
| `popular` | boolean | Observations that have been favorited by at least one user |
| `sounds` | boolean | Observations with sounds |
| `taxon_is_active` | boolean | Observations of active taxon concepts |
| `threatened` | boolean | Observations whose taxa are threatened in their location |
| `verifiable` | boolean | Observations with a `quality_grade` of either `needs_id` or `research`. Equivalent to `quality_grade=needs_id,research` |
| `licensed` | boolean | License attribute of an observation must not be null |
| `photo_licensed` | boolean | License attribute of at least one photo of an observation must not be null |
| `expected_nearby` | boolean | Observation taxon is expected nearby |
| `id` | array di string | Must have this ID |
| `not_id` | array di string | Must not have this ID |
| `license` | array di string | Observation must have this license Valori: cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa, cc0. |
| `ofv_datatype` | array di string | Must have an observation field value with this datatype |
| `photo_license` | array di string | Must have at least one photo with this license Valori: cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa, cc0. |
| `place_id` | array di integer | Must be observed within the place with this ID |
| `project_id` | array di string | Must be added to the project this ID or slug |
| `rank` | array di string | Taxon must have this rank Valori: stateofmatter, kingdom, phylum, subphylum, superclass, class, subclass, superorder, order, suborder, infraorder, superfamily, epifamily, family, subfamily, supertribe, tribe, subtribe, genus, genushybrid, species, hybrid, subspecies, variety, form. |
| `site_id` | array di string | Must be affiliated with the iNaturalist network website with this ID |
| `sound_license` | array di string | Must have at least one sound with this license Valori: cc-by, cc-by-nc, cc-by-nd, cc-by-sa, cc-by-nc-nd, cc-by-nc-sa, cc0. |
| `taxon_id` | array di string | Only show observations of these taxa and their descendants |
| `without_taxon_id` | array di string | Exclude observations of these taxa and their descendants |
| `taxon_name` | array di string | Taxon must have a scientific or common name matching this string |
| `user_id` | array di string | User must have this ID or login |
| `user_login` | array di string | User must have this login |
| `ident_user_id` | integer | Observations identified by a particular user |
| `hour` | array di string | Must be observed within this hour of the day |
| `day` | array di string | Must be observed within this day of the month |
| `month` | array di string | Must be observed within this month |
| `year` | array di string | Must be observed within this year |
| `created_day` | array di string | Must be created within this day of the month |
| `created_month` | array di string | Must be created within this month |
| `created_year` | array di string | Must be created within this year |
| `term_id` | array di integer | Must have an annotation using this controlled term ID |
| `term_value_id` | array di integer | Must have an annotation using this controlled value ID. Must be combined with the `term_id` parameter |
| `without_term_id` | integer | Exclude observations with annotations using this controlled value ID. |
| `without_term_value_id` | array di integer | Exclude observations with annotations using this controlled value ID. Must be combined with the `term_id` parameter |
| `term_id_or_unknown` | array di integer | Must be combined with the `term_value_id` or the `without_term_value_id` parameter. Must have an annotation using this controlled term ID and associated term value IDs or be missing this annotation. |
| `annotation_user_id` | array di string | Must have an annotation created by this user |
| `acc_above` | string | Must have a positional accuracy above this value (meters) |
| `acc_below` | string | Must have a positional accuracy below this value (meters) |
| `acc_below_or_unknown` | string | Positional accuracy must be below this value (in meters) or be unknown |
| `d1` | string | Must be observed on or after this date |
| `d2` | string | Must be observed on or before this date |
| `created_d1` | string | Must be created at or after this time |
| `created_d2` | string | Must be created at or before this time |
| `created_on` | string | Must be created on this date |
| `observed_on` | string | Must be observed on this date |
| `unobserved_by_user_id` | integer | Must not be of a taxon previously observed by this user |
| `apply_project_rules_for` | string | Must match the rules of the project with this ID or slug |
| `cs` | string | Taxon must have this conservation status code. If the `place_id` parameter is also specified, this will only consider statuses specific to that place |
| `csa` | string | Taxon must have a conservation status from this authority. If the `place_id` parameter is also specified, this will only consider statuses specific to that place |
| `csi` | array di string | Taxon must have this IUCN conservation status. If the `place_id` parameter is also specified, this will only consider statuses specific to that place Valori: LC, NT, VU, EN, CR, EW, EX. |
| `geoprivacy` | array di string | Must have this geoprivacy setting Valori: obscured, obscured_private, open, private. |
| `taxon_geoprivacy` | array di string | Filter observations by the most conservative geoprivacy applied by a conservation status associated with one of the taxa proposed in the current identifications. Valori: obscured, obscured_private, open, private. |
| `obscuration` | array di string | Must have `geoprivacy` or `taxon_geoprivacy` fields matching these values Valori: obscured, private, none. |
| `hrank` | string | Taxon must have this rank or lower Valori: stateofmatter, kingdom, phylum, subphylum, superclass, class, subclass, superorder, order, suborder, infraorder, superfamily, epifamily, family, subfamily, supertribe, tribe, subtribe, genus, genushybrid, species, hybrid, subspecies, variety, form. |
| `lrank` | string | Taxon must have this rank or higher Valori: stateofmatter, kingdom, phylum, subphylum, superclass, class, subclass, superorder, order, suborder, infraorder, superfamily, epifamily, family, subfamily, supertribe, tribe, subtribe, genus, genushybrid, species, hybrid, subspecies, variety, form. |
| `iconic_taxa` | array di string | Taxon must by within this iconic taxon Valori: Actinopterygii, Animalia, Amphibia, Arachnida, Aves, Chromista, Fungi, Insecta, Mammalia, Mollusca, Reptilia, Plantae, Protozoa, unknown. |
| `id_above` | string | Must have an ID above this value |
| `id_below` | string | Must have an ID below this value |
| `identifications` | string | Identifications must meet these criteria Valori: most_agree, most_disagree, some_agree. |
| `lat` | number | Must be within a {`radius`} kilometer circle around this lat/lng (*lat, *lng, radius) |
| `lng` | number | Must be within a {`radius`} kilometer circle around this lat/lng (*lat, *lng, radius) |
| `radius` | string | Must be within a {`radius`} kilometer circle around this lat/lng (*lat, *lng, radius) |
| `nelat` | number | Must be within this bounding box (*nelat, *nelng, *swlat, *swlng) |
| `nelng` | number | Must be within this bounding box (*nelat, *nelng, *swlat, *swlng) |
| `swlat` | number | Must be within this bounding box (*nelat, *nelng, *swlat, *swlng) |
| `swlng` | number | Must be within this bounding box (*nelat, *nelng, *swlat, *swlng) |
| `list_id` | integer | Taxon must be in the list with this ID |
| `not_in_project` | string | Must not be in the project with this ID or slug |
| `not_matching_project_rules_for` | string | Must not match the rules of the project with this ID or slug |
| `observation_accuracy_experiment_id` | array di integer | Must included in this observation accuracy experiment |
| `fails_dqa_accurate` | boolean | Must be voted as not accurately depicting an organism or scene |
| `fails_dqa_date` | boolean | Must be voted as not having an accurate date |
| `fails_dqa_evidence` | boolean | Must be voted as not evidence of an organism |
| `fails_dqa_location` | boolean | Must be voted as not having an accurate location |
| `fails_dqa_needs_id` | boolean | Must be voted as the community ID cannot be improved |
| `fails_dqa_recent` | boolean | Must be voted as not recent evidence of an organism |
| `fails_dqa_subject` | boolean | Must be voted as not having evidence related to a single subject |
| `fails_dqa_wild` | boolean | Must be voted as not wild |
| `q` | string | Search observation properties. Can be combined with `search_on` |
| `search_on` | string | Properties to search on, when combined with `q`. Searches across all properties by default Valori: names, tags, description, place. |
| `quality_grade` | string | Must have this quality grade Valori: casual, needs_id, research. |
| `updated_since` | string | Must be updated since this time |
| `viewer_id` | string | See `reviewed` |
| `reviewed` | boolean | Observations have been reviewed by the user with ID equal to the value of the `viewer_id` parameter |
| `locale` | string | Locale preference for taxon common names |
| `preferred_place_id` | integer | Place preference for regional taxon common names |
| `ttl` | string | Set the `Cache-Control` HTTP header with this value as `max-age`, in seconds. This means subsequent identical requests will be cached on iNaturalist servers, and commonly within web browsers |
| `include_ancestors` | boolean | Include taxon ancestors in the response Predefinito: False. |
| `page` | string | Pagination `page` number |
| `per_page` | string | Number of results to return in a `page`. The maximum value is 500 |

## GET https://api.inaturalist.org/v1/taxa/{id}

Taxon Details

Given an ID, or an array of IDs in comma-delimited format, returns
corresponding taxa. A maximum of 30 results will be returned

| Parametro | Tipo | Descrizione |
|---|---|---|
| `id` | array di integer | Must have this ID |
| `rank_level` | number | Taxon must have this rank level. Some example values are 70 (kingdom), 60 (phylum), 50 (class), 40 (order), 30 (family), 20 (genus), 10 (species), 5 (subspecies) |

## GET https://api.inaturalist.org/v1/places/autocomplete

Place Autocomplete

Given an string, returns places with names starting with the search
term.

| Parametro | Tipo | Descrizione |
|---|---|---|
| `q` | string | Search by name (must start with this value) or by ID (exact match). |
| `order_by` | string | Sort field Valori: area. |
