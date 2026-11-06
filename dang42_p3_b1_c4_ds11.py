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


def bt_dang42_p3_b1_c4_ds11(self):
            # Khai báo biến
            # --- Khởi tạo các giá trị ngẫu nhiên ---
            # Chọn ngẫu nhiên cạnh a1 từ 2 đến 10 để số không quá lớn
            a1 = random.randint(2, 10)
            s1 = a1**2
            tong_s = 2 * s1

            # --- Tạo các phương án nhiễu (distractors) ---
            da_dung = '$%s$ cm$^2$' % (latex(tong_s))

            # Các phương án sai phổ biến: 
            # 1. Quên nhân 2 (chỉ tính S1)
            # 2. Nhầm công bội (ví dụ q=1/4 thay vì 1/2) -> S = 4/3 * S1
            # 3. Tính nhầm tổng là 4*S1
            s_sai = [
                '$%s$ cm$^2$' % (latex(s1)),
                '$%s$ cm$^2$' % (latex(3 * s1)),
                '$%s$ cm$^2$' % (latex(4 * s1)),
                '$%s$ cm$^2$' % (latex(round(1.5 * s1, 1))).replace('.', ','),
                '$%s$ cm$^2$' % (latex(tong_s + 4)),
                '$%s$ cm$^2$' % (latex(tong_s - 2)),
            ]

            random.shuffle(s_sai)
            das1 = s_sai[0]
            das2 = s_sai[1]
            das3 = s_sai[2]

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'''\immini{Cho hình vuông $ABCD$ có cạnh bằng $a_1 = %s$ cm và có diện tích $S_1$. Nối 4 trung điểm $A_1, B_1, C_1, D_1$ theo thứ tự của 4 cạnh $AB, BC, CD, DA$ ta được hình vuông thứ hai có diện tích $S_2$. Tiếp tục làm như thế, ta được hình vuông thứ ba là $A_2B_2C_2D_2$ có diện tích $S_3, \dots$ và cứ tiếp tục làm như thế vô hạn. Tổng diện tích các hình vuông được tạo thành bằng bao nhiêu?}
                             {\begin{tikzpicture}
            	\coordinate (A) at (0,4);
            	\coordinate (B) at (0,0);
            	\coordinate (C) at (4,0);
            	\coordinate (D) at (4,4);
            	\coordinate (A1) at (0,2);
            	\coordinate (B1) at (2,0);
            	\coordinate (C1) at (4,2);
            	\coordinate (D1) at (2,4);
            	\coordinate (A2) at (1,1);
            	\coordinate (B2) at (3,1);
            	\coordinate (C2) at (3,3);
            	\coordinate (D2) at (1,3);
            	\coordinate (M1) at (1,2);
            	\coordinate (M2) at (2,1);
            	\coordinate (M3) at (3,2);
            	\coordinate (M4) at (2,3);
            	\draw[line width=1pt] (A) -- (B) -- (C) -- (D) -- cycle;
            	\draw[line width=1pt] (A1) -- (B1) -- (C1) -- (D1) -- cycle;
            	\draw[line width=1pt] (A2) -- (B2) -- (C2) -- (D2) -- cycle;
            	\draw[line width=1pt] (M1) -- (M2) -- (M3) -- (M4) -- cycle;
            	\node[above left] at (A) {$A$};
            	\node[below left] at (B) {$B$};
            	\node[below right] at (C) {$C$};
            	\node[above right] at (D) {$D$};
            	\node[left] at (A1) {$A_1$};
            	\node[below] at (B1) {$B_1$};
            	\node[right] at (C1) {$C_1$};
            	\node[above] at (D1) {$D_1$};
            	\node[below left] at (A2) {$A_2$};
            	\node[below right] at (B2) {$B_2$};
            	\node[above right] at (C2) {$C_2$};
            	\node[above left] at (D2) {$D_2$};
            \end{tikzpicture}}'''
                            % (latex(a1)))

            # --- Nội dung lời giải ---
            loigiai = (r'''Gọi $a_n$ là độ dài cạnh của hình vuông thứ $n$. \\
                      Ta có cạnh của hình vuông sau liên hệ với cạnh hình vuông trước bởi công thức: $a_{n+1} = \sqrt{\left(\frac{a_n}{2}\right)^2 + \left(\frac{a_n}{2}\right)^2} = \frac{a_n\sqrt{2}}{2}$. \\
                      Khi đó diện tích hình vuông thứ $n+1$ là: $S_{n+1} = a_{n+1}^2 = \left(\frac{a_n\sqrt{2}}{2}\right)^2 = \frac{1}{2}a_n^2 = \frac{1}{2}S_n$. \\
                      Như vậy, diện tích các hình vuông lập thành một cấp số nhân lùi vô hạn với số hạng đầu $S_1 = a_1^2 = %s^2 = %s$ và công bội $q = \frac{1}{2}$. \\
                      Tổng diện tích các hình vuông là: $S = \frac{S_1}{1-q} = \frac{%s}{1-\frac{1}{2}} = 2 \cdot %s = %s$ cm$^2$.'''
                      % (latex(a1), latex(s1), latex(s1), latex(s1), latex(tong_s)))

            # --- Xuất kết quả theo định dạng yêu cầu ---
            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(tong_s))

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+ '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

