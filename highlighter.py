import Highlighter from 'web-highlighter';

// won't highlight pre&code elements
const highlighter = new Highlighter({
    exceptSelectors: ['pre', 'code']
});

// add some listeners to handle interaction, such as hover
highlighter
    .on('selection:hover', ({id}) => {
        // display different bg color when hover
        highlighter.addClass('highlight-wrap-hover', id);
    })
    .on('selection:hover-out', ({id}) => {
        // remove the hover effect when leaving
        highlighter.removeClass('highlight-wrap-hover', id);
    })
    .on('selection:create', ({sources}) => {
        sources = sources.map(hs => ({hs}));
        // save to backend
        store.save(sources);
    });

// retrieve data from store, and display highlights on the website
store.getAll().forEach(
    // hs is the same data saved by 'store.save(sources)'
    ({hs}) => highlighter.fromStore(hs.startMeta, hs.endMeta, hs.text, hs.id)
);

// auto-highlight selections
highlighter.run()
