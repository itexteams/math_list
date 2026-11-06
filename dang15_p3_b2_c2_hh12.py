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


def bt_dang15_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                while True:
                    try:
                        # Randomize coordinates of A
                        xA = randint(3, 7) # x-coordinate (East/West)
                        yA = randint(-5, -2) # y-coordinate (North/South) - making it 'South' by being negative
                        zA = randint(2, 5) # z-coordinate (Altitude) - must be positive for initial position


                        xB = randint(-5, -1)
                        yB = randint(-4, -1)
                        zB = randint(1, 4)

                        A = (xA, yA, zA)
                        B = (xB, yB, zB)

                        # vectơ AB = (dx, dy, dz)
                        dx = xB - xA
                        dy = yB - yA
                        dz = zB - zA


                        if dz != 0:
                            t = -Rational(zA, dz)


                            xM = xA + t * dx
                            yM = yA + t * dy

                            # Check for overly complex coordinates (e.g., very large denominators)
                            if abs(t.p) < 1000 and abs(t.q) < 1000:
                                break
                    except Exception:
                        # In case of division by zero or other math errors during randomization
                        pass


                OM_squared = xM**2 + yM**2
                kq2 = sqrt(OM_squared) # Exact result

                # Final result rounded to one decimal place
                kq3 = Decimal(float(kq2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',') # Format for LaTeX output (using comma for decimal)

                # A float value for use in generating distractors
                kq_float = float(kq2)

                # --- Answers and Distractors ---
                # The correct answer
                da = '$\\approx %s \\text{ km}$'%(kq)
                da_d = ('\\True ' + str(da))

                # Distractors (using the float value for simple offsets)
                s_floats = [kq_float + 0.1, kq_float + 0.3, kq_float + 0.5,
                            kq_float - 0.1, kq_float - 0.3, kq_float - 0.5]

                # Rounding and formatting distractors
                s = []
                for val in s_floats:
                    # Avoid creating the correct answer as a distractor
                    distractor_val = Decimal(val).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    if distractor_val != kq3:
                        s.append('$\\approx %s \\text{ km}$'%(str(distractor_val).replace('.',',')))

                # Select 3 unique distractors
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]


                # For a simplified, more general question:
                noidungcauhoi = ('''Trong hệ tọa độ $Oxyz$, gốc $O$ trùng với vị trí chân của tháp trung tâm kiểm soát không lưu, mặt phẳng $(Oxy)$ trùng với mặt đất, trục $Ox$ hướng về phía Đông, trục $Oy$ hướng về phía Bắc. Một máy bay bay theo đường thẳng từ vị trí $A(%s; %s; %s)$ đến vị trí $B(%s; %s; %s)$. Vị trí hạ cánh của máy bay là $M$ thuộc đoạn thẳng $AB$ và nằm trên mặt đất. Khoảng cách từ vị trí hạ cánh $M$ đến vị trí chân của tháp trung tâm kiểm soát không lưu $O$ bằng bao nhiêu kilômét? (làm tròn kết quả đến phần mười).'''
                                 %(latex(xA), latex(yA), latex(zA), latex(xB), latex(yB), latex(zB)))

                # --- Answers List ---
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)


                AB_vec = (dx, dy, dz)

                Mx_num = xA*dz - zA*dx
                My_num = yA*dz - zA*dy
                M_denom = dz

                xM_disp = Rational(Mx_num, M_denom)
                yM_disp = Rational(My_num, M_denom)

                loigiai = ('''Vị trí hạ cánh $M$ nằm trên mặt đất, nên $M$ thuộc mặt phẳng $(Oxy)$, suy ra tọa độ của $M$ có dạng $M(x_M; y_M; 0)$.\\\\
                           Vectơ chỉ phương của đường thẳng $AB$ là $\\vec{u} = \\vec{AB} = (%s; %s; %s)$.\\\\
                           Phương trình tham số của đường thẳng $AB$ là $\\begin{cases} x = %s + %s t \\\\ y = %s + %s t \\\\ z = %s + %s t \\end{cases}$. \\\\
                           Vì $M$ nằm trên đường thẳng $AB$ và $z_M = 0$, ta có:
                           $$%s + %s t = 0 \\Rightarrow  t = - \\frac{%s}{%s} = %s.$$
                           Thay giá trị $t$ vào phương trình tham số, ta được tọa độ điểm $M$ là $\\left(%s; %s; 0\\right)$. \\\\
                           Khoảng cách từ $M$ đến chân tháp $O(0; 0; 0)$ là
                           $$OM = \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2} = \\sqrt{%s} \\approx %s \\text{ km}.$$'''
                           %(latex(dx), latex(dy), latex(dz),
                             latex(xA), latex(dx), latex(yA), latex(dy), latex(zA), latex(dz),
                             latex(zA), latex(dz), latex(zA), latex(dz), latex(t),
                             latex(xM_disp), latex(yM_disp),
                             latex(xM_disp), latex(yM_disp), latex(OM_squared), kq
                           ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # --- Output the Test Question ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content   

