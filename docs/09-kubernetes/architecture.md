# 🏛️ Kubernetes Cluster Architecture

A Kubernetes cluster follows a master-worker architecture consisting of a **Control Plane** (master) and one or more **Worker Nodes**.

---

## 🗺️ 1. Master & Worker Topology Diagram

```mermaid
flowchart TD
    subgraph CONTROL_PLANE["Control Plane (Master Node)"]
        API["kube-apiserver<br/>(Cluster Gateway / REST API)"]
        ETCD[("etcd<br/>(Distributed Key-Value Store)")]
        SCHED["kube-scheduler<br/>(Node Placement Decision Maker)"]
        CM["kube-controller-manager<br/>(Desired State Loop Enforcer)"]
        
        API <--> ETCD
        API <--> SCHED
        API <--> CM
    end

    CLIENT["kubectl CLI / Jenkins Agent"] -- "HTTPS REST Calls" --> API

    subgraph WORKER1["Worker Node 1"]
        KLET1["kubelet"]
        KPRX1["kube-proxy"]
        CR1["Container Runtime (containerd)"]
        POD1["Pod: vprofile-app (Tomcat)"]
        POD2["Pod: vprofile-db (MySQL)"]
        KLET1 --- CR1
        CR1 --- POD1
        CR1 --- POD2
    end

    subgraph WORKER2["Worker Node 2"]
        KLET2["kubelet"]
        KPRX2["kube-proxy"]
        CR2["Container Runtime (containerd)"]
        POD3["Pod: vprofile-app (Tomcat)"]
        KLET2 --- CR2
        CR2 --- POD3
    end

    API <-- "Worker Agent Heartbeat & Commands" --> KLET1
    API <-- "Worker Agent Heartbeat & Commands" --> KLET2
```

---

## ⚙️ 2. Control Plane Components

* **`kube-apiserver`:** The front-end of the Control Plane. Exposes the Kubernetes API; all internal components and external `kubectl` commands communicate strictly through it.
* **`etcd`:** Consistent, highly-available key-value store used as Kubernetes' backing store for all cluster data (state, secrets, configs).
* **`kube-scheduler`:** Watches for newly created Pods with no assigned node and selects the best node for them to run on based on CPU/memory resource availability.
* **`kube-controller-manager`:** Runs controller processes in a continuous reconciliation loop:
  * *Node Controller:* Detects when nodes go offline.
  * *Replication Controller:* Ensures correct replica counts.
  * *Endpoints Controller:* Populates Endpoints objects (joining Services & Pods).

---

## 🏃 3. Worker Node Components

* **`kubelet`:** An agent that runs on each node in the cluster. It ensures that containers are running in a Pod according to the PodSpec.
* **`kube-proxy`:** Network proxy that maintains network rules on nodes, enabling communication to Pods from inside or outside the cluster.
* **Container Runtime:** The software responsible for running containers (e.g. `containerd`, `CRI-O`).
