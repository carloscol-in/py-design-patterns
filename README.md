# Design Patterns Notes

## Factories

A factory is a component responsible solely for the wholesale, or mass creation of objects.

Great when object creation logic becomes too convoluted. Also great when initializer is not descriptive enough about what it's going to be constructing.

More on initializer's shortcomes:

* Name is always __init__
* Can turn into 'optional parameter hell'

Factories are great for wholesale object creation, instead of piecewise, like the Builder. This creation as a wholesale can be outsourced to a method (Factory Method). Or it could also be outsourced to a class, typically, to a Factory. You can also create a hierarchy of factories with Abstract Factory.

## Builder

Build complex classes that require of too many parameters.

## Prototype

A partially of fully initialized object that you copy and make use of. To implement a Prototype you take a partially initialized
object and store it somewhere. Then you make deep copies of this object when it's being tried to instance the object to avoid modifying objects with the same reference. And allow the user to customize the resulting instance either by giving the user some endpoints/methods to do it, or by returning the prototyped object.

> Factories provide a convenient API for using Prototypes.

We make a copy/clone of the prototype and then we customize it to fit our needs.

> Requires 'deep copy' support

We make the cloning convenient, for example, via a Factory.

### Prototype: Motivation

1. Complicated objects aren't designed from scratch
2. An existing design is a Prototype
3. We copy the prototype and customize
4. We want to make cloning convenient

## Singleton

For some components it only makes sense to have one in the system. For example, Database repository or connection, Object factory.

This can solve some performance issues, since the initializer can be expensive resource wise. We provide every user with the same instance of this object that was created once.

You don't want additional copies of this object.

Need to take care of lazy instantiation. You initialize the Singleton instance only when it is needed, and after that every user accesses the same instance.

> A component that is instantiated only once.

### Singleton: Main Concepts

* Multiple ways of implementation of a Singleton; metaclass, decorator, custom allocator.
* Laziness is easy, just init on first request.
* Monostate variation.
* Testability issues.

## Adapter

Getting the interface you want from the interface you have; it's a pattern that helps you adapt the interface that you're given to the interface that you actually need.

An adapter is a construct that adapts an existing interface X to conform to the required interface Y.

You use the adapter pattern when you are given an API to work with, but you want to use a different API.

Whenever your API doesn't match what you're working with, you need to build an inbetween component; an adapter.

## Bridge

Prevents a 'Cartesian product' complexity explosion

A Bridge is a mechanism that aims to decouple an interface (hierarchy) from an implementation (hierarchy).

The main concept is that you can have inheritance and aggregation instead of a complex inheritance tree.

Say for example that you have this classes that you want to implement: Circle, Square. But you want to have variations for this classes, such as colors, or filling, for example. This means that if you wanted to support Red, and Green, you would have this resulting classes.

* RedCircle
* GreenCircle
* RedSquare
* GreenSquare

This isn't scalable. Bridge pattern helps us avoiding this.

> Escape complexity explosion as you get more combinations of multiple classes.

Connects two or more hierarchies of classes using *composition*.

### Bridge: Main Concepts

Decouple the abstraction from the implementation.

Both hierarchies can exist, but you use composition to use them together or combined.

A stronger form of encapsulation.

## Composite

> Treating individual and aggregate objects uniformly. Provide an identical interface for both aggregate components as well as individual components.

### Composite: Motivation

* Objects use other objects' properties/members through inheritance and composition.
* Composition let us make compound objects.
* Composite design pattern is used to treat both single (scalar) and composite objects uniformly.

### Composite: Summary

Composite is a mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.

Premises:

* Objects can use other objects vie inheritance/composition
* Some composed and singular objects need similar/identical behaviors
* Composite design pattern lets us treat both types of objects uniformly
* Python supports iteration with `__iter__(self)`, and the `Iterable` abstract class

## Decorator

> Adding behavior without altering/inheriting the function/class itself.

You usually use the Decorator design pattern when you want to augment an object with additional functionality. Also, when you don't want to rewrite or alter existing code (OCP). It is also a good idea to use the Decorator design pattern when you want to keep the functionality separate (SRP). Sometimes you also want to be able to interact with existing structures or APIs.

There are two options for these motivations:

* Inherit from the required object (if possible)
* Build a Decorator, which simply references the decorated objects (avoids inheritance).

> Facilitates the addition of individual objects' behavior without the need to inherit from them.

## Facade

> Exposing several components through a single interface.

The motivation behind this desing pattern is that you usually want to balance complexity and presentation/usability. You usually use the Facade design pattern when you need to build a simplified interface that performs many other actions behind the scenes.

> Provides a simple, easy to understand/user interface over a large and sophisticated body of code.

You may want to build a Facade to provide a simplified API over a set of classes. And also, it can be ideal to expose internals through the facade. This pattern may allow developers to extend their components functionality by using more complex APIs if they need to.

## Flyweight

This design pattern is all about space optimization. The way it goes about space optimization is that the goal of this design pattern is to avoid data redundancy.

> The Flyweight design pattern is a space optimization technique that lets us use less memory by storing externally the data associated with similar objects.

### Flyweight: Main Concepts

* Store common data externally
* Specify an index or a reference into the external data store
* Define the idea of 'ranges' on __homogeneous collections__ and store data related to those ranges. This way you can apply a given construct to an entire range, and most importantly, save memory resources.

## Proxy

An interface for accessing a particular resource. There are multiple types of proxies:

* Communication proxy
* Logging proxy
* Virtual proxy
* Guarding proxy
* and more...

A Proxy is a class that functions as an interface to a particular resource. That resource may be remote, expensive to construct, or may require logging or some other added functionality.

Virtual Proxy: appears to be the underlying object, but in reality it's not, it's masquerading the underlying functionality, even when not having the underlying functionality. It appears to be the object it's supposed to represent, but behind the scenes it can offer additional functionality and behave differently.

### Proxy vs Decorator

Proxy provides an identical interface to the object that will be consuming this proxy. Decorator on the other hand provides an enhanced interface. The decorator is designed to add behavior, support, additional operations, etc.

Decorator typically aggregates (or has reference to) what it is decorating, which means for example, that the decorator pattern has to either pass a generated object in the constructor or take the decorated object as a constructor argument. Proxy doesn't have to work with a materialized object, you can create a Proxy object without knowing which object it is `Proxying`. Proxy's object doesn't have to exist before creating the proxy, and sometimes, it doesn't even have to exist until the Proxy logic states it should, which is some kind of Lazy Loading.

### Proxy: Main Concepts

* A Proxy object has the same interface as the object it is proxying, or the underlying object.
* To create a Proxy you only have to replicate the interface of an object.
* A Proxy object adds relevant functionality/behavior to the redefined member functions.
* There are different types of Proxies (communication, logging, caching, etc.) that have completely different behaviors.
* There are many use cases on which you could be using Proxies.

## Chain of Responsibility

Sequence of handlers processing an event one after another. A chain of components who all get a chance to process a command or a query, optionally having default processing implementation and an ability to terminate the processing chain.

In some cases you can implement Chain of Responsibility as a Linked List.

### Chain of Responsibility: Command Query Separation

Whenever we operate on objects, we separate all of the invocations into two different concepts; `Query` and `Command`.

A `Command` is something that you send when you're asking for an action or a change.

A `Query` is asking for information, without the necessity to change anything.

`CQS` is a concept that looks for having separate means of sending commands and queries to.

### Chain of Responsibility: Main Concepts

* You can implement Chain of Responsibility design pattern as a Linked-List/Chain of references or a centralized construct.
* Enlist objects in the Chain, possibly controlling their order; either by priority or any other metric. Every element in the Chain can stop the Chain processing and prevent the information from proceeding to other elements of the Chain.
* You can also remove elements from the Chain.

## Command

The motivation of this design pattern is to stop using perishable statements, which are the case for the ordinary statements. This means, that for example, variable assignment is a perishable statement, because you can't undo/rollback to the previous state before executing that statement. This is similar to transaction based state. Another problem that the Command design pattern tries to solve is that you can't serialize sequence of actions (calls). We want an object that represents an operation.

### Command: Use cases

GUI commands, multi-level undo/redo, macro recording, and more. Sometimes called a `Macro`. Sequence of commands that you want to string together.

> A command is an object that represents the instruction to perform certain action. Contains all the necessary information for the action to be taken, as well as for logging purposes if desired.

### Composite Commands

Composite commands is the way to create commands that span more than two members that could have its own command unit each. A Composite Command is a Command, and also a list of Commands.

### Command: Main Concepts

With the Command design pattern you encapsulate all the operation details in a separate object. You can also define the instruction for applying the command, either in the command or somewhere else. You can also construct the functionality to undo the command. With the Command design pattern you can also create sequences of commands, which are usually called `macros`.

## Interpreter

Everything that we do involves the interpretation of text by the computer. The Interpreter design pattern is all about turning text/strings into OOP based structures in a complicated process.

> A component that processes structured data. Does so by turning it into separate lexical tokens (lexing) and then interpreting sequences of said tokens (parsing).

On simple cases, the Interpreter design pattern works in two stages: lexing and parsing.

* Lexing turns text into a set of tokens.
* Parsing tokens into meaningful constructs.

## Iterator

An __iterator__ is a class that facilitates the traversal. An iterator usually keeps a reference to the current element. An iterator knows how to move from the current element to a different element covering all the elements in the Data Structure.

The __iterator__ protocol requires `__iter__()` to expose the iterator, which uses `__next__()` to return each of the iterated elements, or you can raise a `StopIteration` when it's done.

> An object that facilitates the traversal of a Data Structure.
