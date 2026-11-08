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


def bt_dang7_p2_b2_c1_hh12(self):
    # Khởi tạo tọa độ ngẫu nhiên không thẳng hàng cho ba đỉnh A, B, C
    while True:
        xa, ya, za = (
            random.randint(-4, 4),
            random.randint(-4, 4),
            random.randint(0, 2),
        )
        xb, yb, zb = (
            random.randint(-4, 4),
            random.randint(-4, 4),
            random.randint(0, 2),
        )
        xc, yc, zc = (
            random.randint(-4, 4),
            random.randint(-4, 4),
            random.randint(1, 3),
        )
    
        # Tọa độ các vectơ AB, AC
        u1, u2, u3 = xb - xa, yb - ya, zb - za
        v1, v2, v3 = xc - xa, yc - ya, zc - za
    
        # Tích có hướng [AB, AC] để kiểm tra tính thẳng hàng
        cp_x = u2 * v3 - u3 * v2
        cp_y = u3 * v1 - u1 * v3
        cp_z = u1 * v2 - u2 * v1
    
        # Kiểm tra tam giác không suy biến và các điểm phân biệt
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # Tính toán các giá trị liên quan đến bài toán:
    # 1. Tọa độ vectơ AB
    ab_x = xb - xa
    ab_y = yb - ya
    ab_z = zb - za
    
    # 2. Điểm N thỏa mãn BA + BC = 2*BN
    # Ta có BA + BC = 2*BN <=> (A - B) + (C - B) = 2(N - B) <=> A + C - 2B = 2N - 2B <=> 2N = A + C <=> N là trung điểm AC.
    # Cao độ của N:
    z_N_num = za + zc
    z_N_val = Rational(z_N_num, 2)
    
    # 3. Trọng tâm T của tam giác PQR
    # Vì P, Q, R lần lượt là trung điểm của 3 cạnh tam giác ABC, nên trọng tâm T của tam giác PQR trùng với trọng tâm tam giác ABC.
    # Tọa độ trọng tâm: T = (A + B + C)/3
    # Cao độ của T:
    z_T_num = za + zb + zc
    z_T_val = Rational(z_T_num, 3)
    
    # 4. Điểm A là trung điểm của BD => A = (B + D)/2 => D = 2A - B
    xd = 2 * xa - xb
    yd = 2 * ya - yb
    zd = 2 * za - zb
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$ cho tam giác $ABC$ có ba đỉnh $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$. Gọi $P,Q,R$ là trung điểm của ba cạnh tam giác $ABC$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Phát biểu a: Vectơ AB = (ab_x; ab_y; ab_z)
    # Phương án đúng / sai
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    # Sai: làm sai dấu hoặc hoán vị (như nhầm sang OA - OB = -AB)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (-ab_x, -ab_y, -ab_z)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xb, xa, yb, ya, zb, za, ab_x, ab_y, ab_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Phát biểu b: Điểm N thỏa mãn BA + BC = 2 BN thì N có cao độ bằng ...
    if z_N_num % 2 == 0:
        str_z_N = str(z_N_val)
        str_z_N_sai = str(z_N_val + 1)
    else:
        str_z_N = "\\frac{%s}{2}" % z_N_num
        str_z_N_sai = str(z_N_val + 1)
    
    th_da_1_d = (
        "\\True Nếu điểm $N$ thỏa mãn $\\vec{BA} + \\vec{BC} = 2\\vec{BN}$ thì $N$ có cao độ bằng $%s$"
        % (str_z_N)
    )
    th_da_1_s = (
        "Nếu điểm $N$ thỏa mãn $\\vec{BA} + \\vec{BC} = 2\\vec{BN}$ thì $N$ có cao độ bằng $%s$"
        % (str_z_N_sai)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có $\\vec{BA} + \\vec{BC} = 2\\vec{BN} \\Leftrightarrow \\vec{BA} - \\vec{BN} + \\vec{BC} - \\vec{BN} = \\vec{0} \\Leftrightarrow \\vec{NA} + \\vec{NC} = \\vec{0}$. \\\\ Do đó $N$ là trung điểm của đoạn thẳng $AC$. \\\\ Cao độ của điểm $N$ là $z_N = \\frac{z_A + z_C}{2} = \\frac{%s + %s}{2} = %s$."""
        % (za, zc, str_z_N)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Phát biểu c: T là trọng tâm tam giác PQR thì T có cao độ là một số hữu tỷ.
    # Luôn luôn là số hữu tỷ vì tọa độ A, B, C nguyên, z_T = (zA + zB + zC)/3 in Q.
    vd_da_1_d = (
        "\\True $T$ là trọng tâm tam giác $PQR$ thì $T$ có cao độ là một số hữu tỷ"
    )
    vd_da_1_s = (
        "$T$ là trọng tâm tam giác $PQR$ thì $T$ có cao độ là một số vô tỷ"
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    if z_T_num % 3 == 0:
        str_z_T = str(z_T_val)
    else:
        str_z_T = "\\frac{%s}{3}" % z_T_num
    
    loigiai_vd_1 = (
        """Do $P, Q, R$ lần lượt là trung điểm của các cạnh của tam giác $ABC$, nên trọng tâm $T$ của tam giác $PQR$ trùng với trọng tâm của tam giác $ABC$. \\\\ Khi đó cao độ của điểm $T$ được tính theo công thức: $z_T = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + %s + %s}{3} = %s \\in \\mathbb{Q}$. \\\\ Vậy cao độ của $T$ là một số hữu tỷ."""
        % (za, zb, zc, str_z_T)
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Phát biểu d: Điểm A là trung điểm của đoạn thẳng BD thì D(xd; yd; zd)
    vdc_da_1_d = (
        "\\True Điểm $A$ là trung điểm của đoạn thẳng $BD$ thì $D(%s;%s;%s)$"
        % (xd, yd, zd)
    )
    # Tạo tọa độ sai (ví dụ nhầm D là trung điểm AB => D = (A+B)/2 hoặc nhầm D = 2B - A)
    xd_s = 2 * xb - xa
    yd_s = 2 * yb - ya
    zd_s = 2 * zb - za
    vdc_da_1_s = (
        "Điểm $A$ là trung điểm của đoạn thẳng $BD$ thì $D(%s;%s;%s)$"
        % (xd_s, yd_s, zd_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì $A$ là trung điểm của đoạn thẳng $BD$ nên ta có: \\\\ $\\begin{cases} x_A = \\frac{x_B + x_D}{2} \\\\ y_A = \\frac{y_B + y_D}{2} \\\\ z_A = \\frac{z_B + z_D}{2} \\end{cases} \\Leftrightarrow \\begin{cases} x_D = 2x_A - x_B = 2 \\cdot (%s) - (%s) = %s \\\\ y_D = 2y_A - y_B = 2 \\cdot (%s) - (%s) = %s \\\\ z_D = 2z_A - z_B = 2 \\cdot (%s) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $D(%s;%s;%s)$."""
        % (xa, xb, xd, ya, yb, yd, za, zb, zd, xd, yd, zd)
    )
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    
    def count_true_answers(answers):
        return sum("\\True" in ans for ans in answers)
    
    
    # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
    
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        "\\begin{minipage}{\\textwidth} \n"
        "\\begin{ex}\n"
        + str(noidungcauhoi)
        + "\n"
        "\\choiceTFn \n"
        "{" + str(shuffled_answers_nb[0]) + "}\n"
        "{" + str(shuffled_answers_th[0]) + "}\n"
        "{" + str(shuffled_answers_vd[0]) + "}\n"
        "{" + str(shuffled_answers_vdc[0]) + "}\n"
        "\\loigiai{ \n"
        "\\begin{enumEX}[a)]{1} \n"
        "\\item " + str(shuffled_solutions_nb[0]) + "\n"
        "\\item " + str(shuffled_solutions_th[0]) + "\n"
        "\\item " + str(shuffled_solutions_vd[0]) + "\n"
        "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
        "\\end{enumEX}} \n"
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    