import React from 'react';

/**
 * Container-Komponente für dynamische Module.
 * Erwartet ein Array von React-Komponenten und rendert diese nacheinander.
 */
function ModulesContainer({ modules = [] }) {
  return (
    <div className="modules-container">
      {modules.map((Mod, idx) => (
        <Mod key={idx} />
      ))}
    </div>
  );
}

export default ModulesContainer;
