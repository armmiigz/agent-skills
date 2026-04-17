# Component Catalog & Dependencies

This reference provides a list of common shadcn/ui components, their intended use cases, and their primary library dependencies.

## Standard Dependencies
Most components require:
- `lucide-react`: For icons.
- `class-variance-authority` (CVA): For managing styling variants.
- `clsx` & `tailwind-merge`: For combining classes.

## Component Reference

| Component | Suitability | Dependencies |
| :--- | :--- | :--- |
| **Accordion** | Vertically stacked headers that reveal content sections. Use for FAQs. | `@radix-ui/react-accordion` |
| **Alert** | Display a brief, important message to the user. | (None) |
| **AlertDialog** | A modal that interrupts the user with important content and requires an action. | `@radix-ui/react-alert-dialog` |
| **Avatar** | An image element with a fallback for representing the user. | `@radix-ui/react-avatar` |
| **Badge** | Small label for status, tags, or count. | (None) |
| **Button** | Standard interactive element for actions. | `@radix-ui/react-slot` |
| **Calendar** | Date selection. Not for time or date ranges (use specific wrappers). | `react-day-picker`, `date-fns` |
| **Card** | Displays content in a contained container. | (None) |
| **Checkbox** | Control that allows the user to toggle an option. | `@radix-ui/react-checkbox` |
| **Command** | Composable command menu. Ideal for searching long lists or as a Combobox. | `cmdk` |
| **Dialog** | A window overlaid on either the primary window or another dialog window. | `@radix-ui/react-dialog` |
| **DropdownMenu** | Displays a menu to the user triggered by a button. | `@radix-ui/react-dropdown-menu` |
| **Form** | Form implementation using `react-hook-form` and `zod`. | `react-hook-form`, `@hookform/resolvers`, `zod` |
| **Input** | Standard text input. | (None) |
| **Popover** | Displays rich content in a portal, triggered by a button. Non-modal. | `@radix-ui/react-popover` |
| **Select** | Displays a list of options for the user to pick from. | `@radix-ui/react-select` |
| **Sheet** | Extends Dialog to display content that "slides in" from the edge. | `lucide-react` (for close icon) |
| **Skeleton** | Use to show a placeholder while content is loading. | (None) |
| **Switch** | A control that allows the user to toggle between checked and not checked. | `@radix-ui/react-switch` |
| **Table** | Displays data in a grid. Use for simple data. | (None) |
| **Tabs** | A set of layered sections of content, seen one at a time. | `@radix-ui/react-tabs` |
| **Toast** | A succinct message that is displayed temporarily. | `@radix-ui/react-toast` |
| **Tooltip** | A popup that displays information related to an element when it receives keyboard focus or the mouse hovers over it. | `@radix-ui/react-tooltip` |

## Usage Guidelines

### When to use Dialog vs Sheet?
- **Dialog**: For focused tasks where the user needs to interact with a modal in the center of the screen (e.g., "Review Order").
- **Sheet**: For secondary tasks that might benefit from seeing the underlying page content (e.g., "Filter Settings", "Notification List").

### When to use Select vs Command?
- **Select**: When you have a small, fixed list of options (e.g., "Select Month").
- **Command/Combobox**: When you have a large list or need a search feature (e.g., "Select City").

### When to use Tooltip vs Popover?
- **Tooltip**: For single-word or short-phrase descriptions (e.g., "Delete"). Should not contain interactive elements.
- **Popover**: For detailed information or small interactive forms (e.g., "Assign User").
