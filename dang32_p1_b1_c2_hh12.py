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


def bt_dang32_p1_b1_c2_hh12(self):
                def vecto(p1, p2):
                    return Matrix([p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]])

                # Random tọa độ điểm A, B
                A = [randint(-5, 5) for _ in range(3)]
                B = [randint(-5, 5) for _ in range(3)]
                
                # Random pháp tuyến nQ, đảm bảo không phải vecto không
                nq_coeff = [randint(-5, 5) for _ in range(3)]
                while sum(c**2 for c in nq_coeff) == 0:
                    nq_coeff = [randint(-5, 5) for _ in range(3)]
                
                AB = vecto(A, B)
                nq = Matrix(nq_coeff)
                np = AB.cross(nq)

                # Kiểm tra nP không là vecto không (AB không cùng phương nQ)
                while np == Matrix([0, 0, 0]):
                    A = [randint(-5, 5) for _ in range(3)]
                    B = [randint(-5, 5) for _ in range(3)]
                    nq_coeff = [randint(-5, 5) for _ in range(3)]
                    while sum(c**2 for c in nq_coeff) == 0:
                        nq_coeff = [randint(-5, 5) for _ in range(3)]
                    AB = vecto(A, B)
                    nq = Matrix(nq_coeff)
                    np = AB.cross(nq)

                # --- PHẦN SỬA LỖI HIỂN THỊ PHƯƠNG TRÌNH (Q) ---
                def format_plane_eq(coeffs, constant):
                    vars = ['x', 'y', 'z']
                    parts = []
                    for i in range(3):
                        c = coeffs[i]
                        if c == 0: continue
                        
                        # Xử lý dấu và hệ số
                        if c == 1:
                            term = vars[i]
                        elif c == -1:
                            term = "-" + vars[i]
                        else:
                            term = f"{c}{vars[i]}"
                        
                        # Thêm dấu nối nếu không phải số hạng đầu tiên
                        if parts and c > 0:
                            parts.append("+" + term)
                        else:
                            parts.append(term)
                    
                    eq = "".join(parts)
                    if constant > 0:
                        eq += f"+{constant}"
                    elif constant < 0:
                        eq += f"{constant}"
                    return eq + "=0"

                d = randint(-5, 5)
                q_eq = format_plane_eq(nq_coeff, d)
                # ----------------------------------------------

                # Format hiển thị tọa độ
                A_latex = "(%s;%s;%s)" % (latex(A[0]), latex(A[1]), latex(A[2]))
                B_latex = "(%s;%s;%s)" % (latex(B[0]), latex(B[1]), latex(B[2]))
                nq_latex = "(%s;%s;%s)" % (latex(nq[0]), latex(nq[1]), latex(nq[2]))
                np_latex = "(%s;%s;%s)" % (latex(np[0]), latex(np[1]), latex(np[2]))
                AB_latex = "(%s;%s;%s)" % (latex(AB[0]), latex(AB[1]), latex(AB[2]))

                # Đáp án đúng và sai
                kq_np_latex = "$%s$" % (np_latex)
                s = []
                while len(s) < 3:
                    err = np + Matrix([randint(-3, 3) for _ in range(3)])
                    if err != np and err.tolist() not in [x.tolist() for x in s]:
                        s.append(err)
                
                das = ["$(%s;%s;%s)$" % (latex(v[0]), latex(v[1]), latex(v[2])) for v in s]

                noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(P)$ đi qua hai điểm $A%s$, $B%s$ và vuông góc với mặt phẳng $(Q): %s$. Khi đó mặt phẳng $(P)$ có một vectơ pháp tuyến là'''
                                %(A_latex, B_latex, q_eq))

                da_d = ('\\True ' + str(kq_np_latex))
                list_1 = [da_d, das[0], das[1], das[2]]
                random.shuffle(list_1)

                loigiai=('''Mặt phẳng $(Q)$ có vectơ pháp tuyến là $\\vec{n}_Q = %s$. \\\\
Vectơ $\\vec{AB} = %s$. \\\\
Mặt phẳng $(P)$ đi qua hai điểm $A, B$ và vuông góc với mặt phẳng $(Q)$ nên có cặp vectơ chỉ phương là $\\vec{AB}$ và $\\vec{n}_Q$. \\\\
Do đó $(P)$ có một vectơ pháp tuyến là $\\vec{n}_P = [\\vec{AB}, \\vec{n}_Q] = %s$.''' 
                % (nq_latex, AB_latex, np_latex))

                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                    '\\choice \n'
                    '{'+str(list_1[0])+'}\n'
                    '{'+str(list_1[1])+'}\n'
                    '{'+str(list_1[2])+'}\n'
                    '{'+str(list_1[3])+'}\n'
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
                return content