<template>
  <div class="version-section">
    <div class="ui grid">
      <div class="four wide column">
        <img
          class="ui small rounded image"
          title="placeholder"
          alt="placeholder"
          src="/static/images/placeholder.png"
        />
      </div>
      <div class="ten wide column">
        <h4>
          <a :href="archive_link">
            <i class="right floated file archive outline icon"></i>
          </a>
          <router-link :to="`/t/${team}/${gameSlug}/${slug}`">
            {{ name }}
          </router-link>
        </h4>
        <div class="description">
          <RenderedMarkdown :body="changelog" />
        </div>
      </div>
      <div class="two wide column right aligned">
        <i
          title="delete"
          class="trash alternate icon"
          v-if="permissions['this:delete']"
        ></i>
        <i
          title="edit"
          class="pencil alternate icon"
          v-if="permissions['this:edit']"
        ></i>
      </div>
    </div>
    <h4 class="ui horizontal divider">
      files
    </h4>
    <ul>
      <li v-for="file in attachedFiles" :key="file.id">
        <a :href="file.attached_file">
          <i class="file pdf outline icon"></i> {{ file.name }}
        </a>
      </li>
    </ul>
    <h4 class="ui horizontal divider">
      coming soon: discussion
    </h4>
    <div class="ui raised segment">
      <div class="ui placeholder">
        <div class="image header">
          <div class="line"></div>
          <div class="line"></div>
        </div>
        <div class="paragraph">
          <div class="medium line"></div>
          <div class="short line"></div>
        </div>
      </div>
    </div>
    <div class="ui raised segment">
      <div class="ui placeholder">
        <div class="image header">
          <div class="line"></div>
          <div class="line"></div>
        </div>
        <div class="paragraph">
          <div class="medium line"></div>
          <div class="short line"></div>
        </div>
      </div>
    </div>
    <div class="ui raised segment">
      <div class="ui placeholder">
        <div class="image header">
          <div class="line"></div>
          <div class="line"></div>
        </div>
        <div class="paragraph">
          <div class="medium line"></div>
          <div class="short line"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'VersionSection',
  props: {
    id: String,
    name: String,
    team: String,
    gameSlug: String,
    slug: String,
    changelog: String,
    archive_link: String,
    permissions: Object,
    attachedFiles: Array,
  },
  components: { RenderedMarkdown },
};
</script>
