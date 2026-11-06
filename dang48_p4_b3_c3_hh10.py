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


def bt_dang48_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập các giá trị cố định theo đề bài
                # Đường thẳng d: x - y + 1 = 0 => y = x + 1. M(a, a+1)
                # Đường tròn (C): x^2 + y^2 - 2x + 4y - 4 = 0
                # Tâm I(1, -2), R^2 = 1^2 + (-2)^2 - (-4) = 9

                a_val = Rational(-3, 2)
                m_y_val = Rational(-1, 2)

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường thẳng $d: x - y + 1 = 0$ và đường tròn $(C): x^2 + y^2 - 2x + 4y - 4 = 0$. Tìm tọa độ điểm $M \in d$ sao cho từ $M$ kẻ được hai tiếp tuyến $MA, MB$ thỏa mãn khoảng cách từ $N\left( 0; \frac{1}{2} \right)$ đến đường thẳng $AB$ lớn nhất.''')

                # Đáp án đúng và các đáp án nhiễu
                da = r'$M\left( -\frac{3}{2}; -\frac{1}{2} \right)$'
                s = [
                    r'$M\left( \frac{3}{2}; \frac{5}{2} \right)$',
                    r'$M\left( 0; 1 \right)$',
                    r'$M\left( 1; 2 \right)$',
                    r'$M\left( -1; 0 \right)$',
                    r'$M\left( -2; -1 \right)$'
                ]

                da_d = ('\\True ' + str(da))
                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Đưa các đáp án vào danh sách
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Đường tròn $(C)$ có tâm $I(1; -2)$. Ta có điểm $M$ thuộc $d$ nên $M(a; a+1)$. \\
            Gọi $K$ là trung điểm của $MI$ thì $K\left( \frac{a+1}{2}; \frac{a-1}{2} \right)$. \\
            Vì tam giác $\triangle MAI, \triangle MBI$ vuông tại $A, B$ nên $KA = KB = \frac{1}{2}MI$. \\
            Đường tròn $(C')$ tâm $K$, đường kính $MI$ nên có phương trình: \\
            $\left( x - \frac{a+1}{2} \right)^2 + \left( y - \frac{a-1}{2} \right)^2 = \frac{a^2+2a+5}{2} \Leftrightarrow x^2 + y^2 - (a+1)x - (a-1)y - a - 2 = 0$. \\
            Đường thẳng $AB$ là giao của $(C) \cap (C')$ nên tọa độ điểm $A, B$ thỏa mãn hệ: \\
            $\begin{cases} x^2 + y^2 - 2x + 4y - 4 = 0 \\ x^2 + y^2 - (a+1)x - (a-1)y - a - 2 = 0 \end{cases} \Rightarrow (1-a)x - (a+3)y - a + 2 = 0$. \\
            Suy ra đường thẳng $AB$ có phương trình $(1-a)x - (a+3)y - a + 2 = 0$. \\
            Khoảng cách từ $N$ đến $AB$ là: \\
            $d_{(N; AB)} = \frac{|7-a|}{2\sqrt{(1-a)^2 + (a+3)^2}} = \frac{1}{2}\sqrt{\frac{a^2-14a+49}{2a^2+4a+10}} = \frac{1}{2}\sqrt{4 \left[ \frac{34}{16} - \frac{(2a+3)^2}{2a^2+4a+10} \right]} \le \frac{\sqrt{34}}{4}$. \\
            $\max f(a) = \frac{\sqrt{34}}{4} \Leftrightarrow a = -\frac{3}{2}$. \\
            Vậy $M\left( -\frac{3}{2}; -\frac{1}{2} \right)$.''')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

