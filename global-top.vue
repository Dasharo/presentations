<template>
  <div>
    <Scroll />
    <footer
      v-if="$nav.currentLayout !== 'cover'"
      class="absolute bottom-0 left-0 right-0 flex justify-between items-center py-2 text-[#000000]"
    >
      <small>© 2025 3mdeb Sp. z o.o. Licensed under the <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">CC BY-SA 4.0</a>. .
</small>
      <small class="mr-4">{{ $nav.currentPage }}</small>
    </footer>
  </div>
</template>
