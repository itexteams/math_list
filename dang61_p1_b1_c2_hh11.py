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


def bt_dang61_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến hình học
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random hóa bài toán bằng cách thay đổi giá trị cạnh a
                # Ở đây ta chọn a là một số nguyên từ 2 đến 10 để đa dạng đề bài
                a_val = random.randint(2, 9)
                a = a_val
                bc_val = latex(sqrt(2 * a**2)) # a*sqrt(2)

                # Kết quả góc luôn là 60 độ với cấu hình hình học này
                kq_goc = 60

                # Các đáp án trắc nghiệm
                da = '$%s^\\circ$' % (kq_goc)

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s = ['$30^\\circ$', '$45^\\circ$', '$90^\\circ$', '$120^\\circ$', '$150^\\circ$']

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Hình vẽ TikZ cho hình chóp S.ABC
                tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (4,0);
                \\coordinate (C) at (1.5,-1.5);
                \\coordinate (I) at ($(B)!0.5!(C)$);
                \\coordinate (S) at ($(I)+(0,4)$);
                \\draw[dashed] (A) -- (B);
                \\draw (S) -- (A) -- (C) -- (B) -- (S) -- (C) (S) -- (I);
                \\filldraw (S) node[above] {$S$};
                \\filldraw (A) node[left] {$A$};
                \\filldraw (B) node[right] {$B$};
                \\filldraw (C) node[below] {$C$};
                \\filldraw (I) node[below right] {$I$};
            \\end{tikzpicture}
            \\end{center}''')

                # Bước 2: Viết lại nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABC$ có độ dài các cạnh $SA = SB = SC = AB = AC = %s$ và $BC = %s$. Góc giữa hai đường thẳng $AB$ và $SC$ là'''
                                 % (latex(a), bc_val))


                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Viết lại nội dung lời giải chi tiết (Không viết tắt)
                loigiai = ('''Ta có $AB^2 + AC^2 = %s^2 + %s^2 = %s$, $BC^2 = (%s)^2 = %s$. \\\\
                             Vì $AB^2 + AC^2 = BC^2$ nên tam giác $ABC$ vuông tại $A$. \\\\
                             Vì $SA = SB = SC = %s$ nên hình chiếu vuông góc của $S$ lên mặt phẳng $(ABC)$ trùng với tâm $I$ của đường tròn ngoại tiếp tam giác $ABC$. \\\\
                             Tam giác $ABC$ vuông tại $A$ nên $I$ là trung điểm của $BC$. \\\\
                             Ta có $\\cos(AB, SC) = |\\cos(\\vec{AB}, \\vec{SC})| = \\frac{|\\vec{AB} \\cdot \\vec{SC}|}{AB \\cdot SC}$. \\\\
                             Xét tích vô hướng: $\\vec{AB} \\cdot \\vec{SC} = \\vec{AB}(\\vec{SI} + \\vec{IC}) = \\vec{AB} \\cdot \\vec{SI} + \\vec{AB} \\cdot \\vec{IC}$. \\\\
                             Vì $SI \\perp (ABC) \\Rightarrow SI \\perp AB \\Rightarrow \\vec{AB} \\cdot \\vec{SI} = 0$. \\\\
                             Do đó $\\vec{AB} \\cdot \\vec{SC} = \\vec{AB} \\cdot \\vec{IC} = -\\vec{BA} \\cdot \\frac{1}{2}\\vec{BC} = -\\frac{1}{2} BA \\cdot BC \\cdot \\cos 45^\\circ$. \\\\
                             $\\vec{AB} \\cdot \\vec{SC} = -\\frac{1}{2} \\cdot %s \\cdot %s \\cdot \\frac{\\sqrt{2}}{2} = -\\frac{%s}{2}$. \\\\
                             Khi đó $\\cos(AB, SC) = \\frac{|-%s/2|}{%s \\cdot %s} = \\frac{1}{2}$. \\\\
                             Suy ra góc giữa hai đường thẳng $AB$ và $SC$ bằng $60^\\circ$.'''
                           % (latex(a), latex(a), latex(2*a**2), bc_val, latex(2*a**2),
                              latex(a), latex(a), bc_val, latex(a**2),
                              latex(a**2), latex(a), latex(a)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' +tikz_code+ str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

