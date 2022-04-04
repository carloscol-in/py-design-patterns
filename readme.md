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

### Motivation

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

### Main Concepts

* Multiple ways of implementation of a Singleton; metaclass, decorator, custom allocator.
* Laziness is easy, just init on first request.
* Monostate variation.
* Testability issues.
