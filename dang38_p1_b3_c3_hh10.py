import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang38_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Thiết lập các giá trị cố định theo đề bài
            xI, yI = 2, -1
            R2 = 8
            IH2 = R2

            # Tính toán IA và IB
            # 1/IA^2 + 1/(2*IA)^2 = 1/8 => 5/(4*IA^2) = 1/8 => IA^2 = 10 => IA = sqrt(10)
            # IB^2 = 4 * IA^2 = 40 => IB = 2*sqrt(10)

            IA_val = sqrt(10)
            IB_val = 2*sqrt(10)

            # Điểm A thuộc d: x - 2y + 3 = 0 => A(2a-3; a)
            # IA^2 = 10 <=> (2a-3-2)^2 + (a+1)^2 = 10 <=> (2a-5)^2 + (a+1)^2 = 10
            # 5a^2 - 18a + 16 = 0 => a = 2 hoặc a = 8/5
            # Điều kiện hoành độ xA >= 2: 
            # Với a = 2 => xA = 2*2 - 3 = 1 (Loại theo hình ảnh/lời giải mẫu có xA >= 2, 
            # Tuy nhiên lời giải trong ảnh ghi A(1;2) và xA >= 2 là mâu thuẫn. 
            # Tôi sẽ bám sát tọa độ kết quả trong ảnh: A(1;2), B(8;1), C(3;-4), D(-4;-3))

            A = (1, 2)
            B = (8, 1)
            C = (3, -4)
            D = (-4, -3)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Trong mặt phẳng $Oxy$, cho hình thoi $ABCD$ ngoại tiếp đường tròn $(C)$ có phương trình $(x-2)^2+(y+1)^2=8$ và điểm $A$ thuộc đường thẳng $d:x-2y+3=0$. Tọa độ các đỉnh của hình thoi, biết rằng $BD=2AC$ và tung độ điểm $A$ không nhỏ hơn $2$ là'''

            # Các đáp án (Lấy kết quả đúng và tạo các phương án nhiễu)
            da_dung = r'$A(1;2), B(8;1), C(3;-4), D(-4;-3)$'
            da_sai1 = r'$A(1;2), B(4;5), C(3;-4), D(-2;-1)$'
            da_sai2 = r'$A(1;2), B(6;3), C(3;-4), D(-6;-5)$'
            da_sai3 = r'$A(1;2), B(0;7), C(3;-4), D(1;-5)$'

            da_d = r'\True ' + da_dung
            list_1 = [da_d, da_sai1, da_sai2, da_sai3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = r'''Đường tròn $(C)$ có tâm $I(2;-1)$, bán kính $R=IH=2\sqrt{2}$.\\
            Vì $ABCD$ là hình thoi nên $AC \perp BD$ tại trung điểm $I$ của mỗi đường. Ta có $BD=2AC \Rightarrow IB=2IA$.\\
            Trong tam giác vuông $IAB$, ta có: $\frac{1}{IA^2} + \frac{1}{IB^2} = \frac{1}{IH^2} \Rightarrow \frac{5}{4IA^2} = \frac{1}{8} \Rightarrow \begin{cases} IA = \sqrt{10} \\ IB = 2\sqrt{10} \end{cases}$.\\
            Giả sử $A(2a-3;a) \in d$. Từ $IA^2=10 \Rightarrow (2a-5)^2+(a+1)^2=10 \Rightarrow 5a^2-18a+16=0 \Rightarrow a=2$ hoặc $a=\frac{8}{5}$.\\
            Kết hợp điều kiện $y_A \geq 2$ ta chọn $A(1;2)$. Suy ra $C(3;-4)$ (do $I$ là trung điểm $AC$).\\
            Phương trình đường thẳng $BD$ đi qua $I(2;-1)$ và vuông góc với $IA$ là: $x-3y-5=0$.\\
            Tọa độ các điểm $B, D$ là nghiệm của hệ: $\begin{cases} x-3y-5=0 \\ (x-2)^2+(y+1)^2=40 \end{cases} \Rightarrow \begin{cases} x=8; y=1 \\ x=-4; y=-3 \end{cases}$.\\
            Vậy tọa độ các đỉnh là \\ $A(1;2), B(8;1), C(3;-4), D(-4;-3)$ hoặc $A(1;2), B(-4;-3), C(3;-4), D(8;1)$.'''

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

