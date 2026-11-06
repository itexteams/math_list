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


def bt_dang46_p3_b1_c5_ds10(self):
            # Chọn ngẫu nhiên 5 chữ số khác nhau từ 1 đến 9
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random chiều dài các tuyến cáp quang (từ 1 đến 6 km)
                e1 = random.randint(1, 6) # Cạnh AB
                e2 = random.randint(1, 6) # Cạnh AC
                e3 = random.randint(1, 6) # Cạnh BC
                e4 = random.randint(1, 6) # Cạnh AD
                e5 = random.randint(1, 6) # Cạnh BE
                e6 = random.randint(1, 6) # Cạnh CE
                e7 = random.randint(1, 6) # Cạnh DE

                # Áp dụng thuật toán Floyd-Warshall để tìm đường đi ngắn nhất giữa mọi cặp đỉnh
                # Quy ước đỉnh: 0:A, 1:B, 2:C, 3:D, 4:E
                INF = 10000
                dist = [[INF] * 5 for _ in range(5)]
                for i in range(5): 
                    dist[i][i] = 0

                edges_list = [(0,1,e1), (0,2,e2), (1,2,e3), (0,3,e4), (1,4,e5), (2,4,e6), (3,4,e7)]
                for u, v, w in edges_list:
                    dist[u][v] = w
                    dist[v][u] = w

                for k in range(5):
                    for i in range(5):
                        for j in range(5):
                            if dist[i][j] > dist[i][k] + dist[k][j]:
                                dist[i][j] = dist[i][k] + dist[k][j]

                # Các đỉnh có bậc lẻ luôn là A(0), B(1), C(2), E(4). Đỉnh D(3) có bậc 2.
                # Tính chi phí cho 3 cách ghép cặp các đỉnh bậc lẻ
                cost1 = dist[0][1] + dist[2][4] # Cặp (A,B) và (C,E)
                cost2 = dist[0][2] + dist[1][4] # Cặp (A,C) và (B,E)
                cost3 = dist[0][4] + dist[1][2] # Cặp (A,E) và (B,C)

                min_extra = min(cost1, cost2, cost3)
                total_sum = e1 + e2 + e3 + e4 + e5 + e6 + e7
                ans = total_sum + min_extra

                kq = str(ans)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Sinh ngẫu nhiên các phương án sai khác nhau
                sai_vals = []
                while len(sai_vals) < 3:
                    offset = random.choice([-4, -3, -2, -1, 1, 2, 3, 4, 5])
                    sai_val = ans + offset
                    if sai_val != ans and sai_val not in sai_vals and sai_val > 0:
                        sai_vals.append(sai_val)

                das1 = '$%s$' % sai_vals[0]
                das2 = '$%s$' % sai_vals[1]
                das3 = '$%s$' % sai_vals[2]

                # Câu hỏi (chú ý sử dụng \\ cho các lệnh LaTeX để tránh lỗi string)
                noidungcauhoi = ('''Tại một khu trung tâm dữ liệu, kỹ sư IT cần kiểm tra kết nối giữa các máy chủ trong hệ thống gồm các trạm $A, B, C, D, E$. Các tuyến cáp quang nối giữa các trạm được biểu diễn trong sơ đồ sau, với chữ số ghi trên mỗi tuyến là chiều dài dây cáp (đơn vị: kilômét). Kỹ sư cần thực hiện một hành trình bắt đầu từ một trạm bất kỳ, đi qua tất cả các tuyến cáp ít nhất một lần và kết thúc tại đúng trạm khởi hành, nhằm đảm bảo toàn bộ hệ thống được kiểm tra. Tổng chiều dài đường đi ngắn nhất mà kỹ sư cần di chuyển là bao nhiêu kilômét?
            \\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt]
            \\coordinate (A) at (0,3);
            \\coordinate (B) at (3,4.5);
            \\coordinate (C) at (5.5,3);
            \\coordinate (D) at (0.2,0);
            \\coordinate (E) at (4.5,-0.5);
            \\draw (A) node[left]{$A$} -- (B) node[above]{$B$} node[midway, above left]{$%s$}
                  -- (C) node[right]{$C$} node[midway, above right]{$%s$};
            \\draw (A) -- (C) node[midway, below]{$%s$};
            \\draw (A) -- (D) node[left]{$D$} node[midway, left]{$%s$};
            \\draw (B) -- (E) node[right]{$E$} node[pos=0.7, left]{$%s$};
            \\draw (C) -- (E) node[midway, right]{$%s$};
            \\draw (D) -- (E) node[midway, below]{$%s$};
            \\fill (A) circle (2pt);
            \\fill (B) circle (2pt);
            \\fill (C) circle (2pt);
            \\fill (D) circle (2pt);
            \\fill (E) circle (2pt);
            \\end{tikzpicture}
            \\end{center}''' % (e1, e3, e2, e4, e5, e6, e7))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Bài toán yêu cầu tìm hành trình đi qua tất cả các cạnh ít nhất một lần với tổng chiều dài nhỏ nhất (Bài toán đường đi người đưa thư Trung Hoa).\\\\
            Tổng chiều dài tất cả các tuyến cáp là:
            $S = %s + %s + %s + %s + %s + %s + %s = %s$ km.\\\\
            Bậc của các đỉnh trong đồ thị:\\\\
            - Đỉnh $A$: bậc $3$ (lẻ).\\\\
            - Đỉnh $B$: bậc $3$ (lẻ).\\\\
            - Đỉnh $C$: bậc $3$ (lẻ).\\\\
            - Đỉnh $D$: bậc $2$ (chẵn).\\\\
            - Đỉnh $E$: bậc $3$ (lẻ).\\\\
            Các đỉnh có bậc lẻ là $A, B, C, E$. Để có thể đi qua mọi cạnh và quay về điểm xuất phát, ta cần lặp lại một số đoạn đường nối các cặp đỉnh bậc lẻ sao cho tổng chiều dài thêm vào là nhỏ nhất.\\\\
            Có $3$ cách ghép cặp các đỉnh bậc lẻ:\\\\
            \\textbf{Cách 1:} Cặp $\\left(A, B\\right)$ và $\\left(C, E\\right)$. Chi phí đi thêm: $d\\left(A, B\\right) + d\\left(C, E\\right) = %s + %s = %s$.\\\\
            \\textbf{Cách 2:} Cặp $\\left(A, C\\right)$ và $\\left(B, E\\right)$. Chi phí đi thêm: $d\\left(A, C\\right) + d\\left(B, E\\right) = %s + %s = %s$.\\\\
            \\textbf{Cách 3:} Cặp $\\left(A, E\\right)$ và $\\left(B, C\\right)$. Chi phí đi thêm: $d\\left(A, E\\right) + d\\left(B, C\\right) = %s + %s = %s$.\\\\
            Khoảng cách tăng thêm nhỏ nhất là $\\min\\left(%s, %s, %s\\right) = %s$.\\\\
            Tổng chiều dài đường đi ngắn nhất mà kỹ sư cần di chuyển là:
            $%s + %s = %s$ km.'''
                %(e1, e2, e3, e4, e5, e6, e7, total_sum,
                  dist[0][1], dist[2][4], cost1,
                  dist[0][2], dist[1][4], cost2,
                  dist[0][4], dist[1][2], cost3,
                  cost1, cost2, cost3, min_extra,
                  total_sum, min_extra, ans
                 ))
                dapan='\\shortans[0]{$%s$}\n'%(ans)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

