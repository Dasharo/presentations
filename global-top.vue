<template>
  <div>
    <Scroll/>
    <footer
      v-if="$nav.currentLayout !== 'cover'"
      class="absolute bottom-0 left-0 right-0 text-center py-2 text-[#000000]"
    >
      <small>© 2025 3mdeb Sp. z o.o. Licensed under the <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">CC BY-SA 4.0</a>.
</small>
      <div class="absolute bottom-0 right-0 py-2 pr-2 text-right text-[#000000]">
        <small><SlideCurrentNo/>/<SlidesTotal/></small>
      </div>
    </footer>
  </div>
</template>
