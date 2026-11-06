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


def bt_dang29_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và sinh dữ liệu ngẫu nhiên
            # Chọn hệ số cho hệ bất phương trình sao cho tạo thành tứ giác OABC ở góc phần tư thứ nhất
            pairs_ineq = [(10, 8), (14, 10), (16, 14), (20, 16)]
            c1, c2 = random.choice(pairs_ineq)

            x_B = int((2*c2 - c1) / 3)
            y_B = int((2*c1 - c2) / 3)

            x_A = int(c2/2)
            y_C = int(c1/2)

            # Hệ số hàm mục tiêu F(x, y) = m*x + n*y
            m = random.choice([3, 4, 5])
            n = random.choice([2, 3, 4])
            F_max = m*x_B + n*y_B

            # Random điểm để kiểm tra nghiệm
            nb_x_false = x_B + 1
            nb_y_false = y_B + 2
            nb_x_true = x_B - 1
            nb_y_true = y_B - 1

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình bậc nhất hai ẩn $\\begin{cases} x + 2y - %s \\le 0 \\\\ 2x + y - %s \\le 0 \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$ $(I)$ và $F(x,y)=%sx+%sy$ với $x;y$ thỏa hệ bất phương trình $(I)$.''' % (c1, c2, m, n))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_s = 'Cặp số $(x;y)=(%s;%s)$ là nghiệm của bất phương trình $(I)$' % (nb_x_false, nb_y_false)
            nb_da_1_d = '\\True Cặp số $(x;y)=(%s;%s)$ là nghiệm của bất phương trình $(I)$' % (nb_x_true, nb_y_true)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1_d = ('''Thay $x = %s, y = %s$ vào hệ bất phương trình $(I)$ ta được: \\\\
            $\\begin{cases} %s + 2 \\cdot %s - %s = %s \\le 0 \\\\ 2 \\cdot %s + %s - %s = %s \\le 0 \\\\ %s \\ge 0 \\\\ %s \\ge 0 \\end{cases}$ (thỏa mãn). \\\\
            Vậy $(%s;%s)$ là một nghiệm của bất phương trình $(I)$.''' % (nb_x_true, nb_y_true, nb_x_true, nb_y_true, c1, nb_x_true+2*nb_y_true-c1, nb_x_true, nb_y_true, c2, 2*nb_x_true+nb_y_true-c2, nb_x_true, nb_y_true, nb_x_true, nb_y_true))

            loigiai_nb_1_s = ('''Thay $x = %s, y = %s$ vào hệ bất phương trình $(I)$ ta thấy không thỏa mãn. \\\\
            Vậy $(%s;%s)$ không là nghiệm của bất phương trình $(I)$.''' % (nb_x_false, nb_y_false, nb_x_false, nb_y_false))

            loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_s = 'Miền nghiệm của hệ bất phương trình không chứa gốc tọa độ $O$'
            th_da_1_d = '\\True Miền nghiệm của hệ bất phương trình chứa gốc tọa độ $O$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1_d = ('''Thay $x = 0, y = 0$ vào hệ bất phương trình $(I)$ ta được: \\\\
            $\\begin{cases} 0 + 2 \\cdot 0 - %s = -%s \\le 0 \\\\ 2 \\cdot 0 + 0 - %s = -%s \\le 0 \\\\ 0 \\ge 0 \\\\ 0 \\ge 0 \\end{cases}$ (luôn đúng). \\\\
            Vậy miền nghiệm của hệ bất phương trình chứa gốc tọa độ $O(0;0)$.''' % (c1, c1, c2, c2))

            loigiai_th_1_s = ('''Thay $x = 0, y = 0$ vào hệ bất phương trình $(I)$ ta thấy thỏa mãn. \\\\
            Vậy miền nghiệm của hệ bất phương trình phải chứa gốc tọa độ $O(0;0)$. Khẳng định trên là sai.''' % ())

            loigiai_th_1 = loigiai_th_1_d if th_da_1 == th_da_1_d else loigiai_th_1_s
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Miền nghiệm của hệ bất phương trình là tứ giác $OABC$ với $O(0;0); A(%s;0); B(%s;%s); C(0;%s)$' % (x_A, x_B, y_B, y_C)
            vd_da_1_s = 'Miền nghiệm của hệ bất phương trình là tứ giác $OABC$ với $O(0;0); A(%s;0); B(%s;%s); C(0;%s)$' % (x_A+1, x_B, y_B, y_C)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Kích thước vùng vẽ TikZ
            x_max = max(c1, c2) + 2
            y_max = max(c1, c2) + 2

            # Tọa độ đầu mút đường thẳng d1: x + 2y - c1 = 0
            d1_y_start = (c1 + 2) / 2
            d1_y_end = (-x_max + c1) / 2

            # Tọa độ đầu mút đường thẳng d2: 2x + y - c2 = 0
            d2_y_start = c2 + 4
            d2_y_end = c2 - 2 * x_max

            loigiai_vd_1_d = ('''Vẽ các đường thẳng $d_1: x+2y-%s=0$, $d_2: 2x+y-%s=0$, $x=0$, $y=0$ và xác định các nửa mặt phẳng thỏa mãn.
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.4, line width=1pt]
            \\draw[->] (-2, 0) -- (%s, 0) node[below] {$x$};
            \\draw[->] (0, -2) -- (0, %s) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (%s,%s);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (%s,%s);
            \\fill[white] (0,0) -- (%s,0) -- (%s,%s) -- (0,%s) -- cycle;
            \\draw[black] (-2,%s) -- (%s,%s); 
            \\draw[black] (-2,%s) -- (%s,%s);  
            \\draw[black] (0,-2) -- (0,%s); 
            \\draw[black] (-2,0) -- (%s,0); 
            \\coordinate (O) at (0,0);
            \\coordinate (A) at (%s,0);
            \\coordinate (B) at (%s,%s);
            \\coordinate (C) at (0,%s);
            \\fill (O) circle (3.5pt) node[below left] {$O$};
            \\fill (A) circle (3.5pt) node[below right] {$A$};
            \\fill (B) circle (3.5pt) node[above right] {$B$};
            \\fill (C) circle (3.5pt) node[above left] {$C$};
            \\end{tikzpicture}
            \\end{center}
            Miền nghiệm của hệ bất phương trình là tứ giác $OABC$ với $O(0;0); A(%s;0); B(%s;%s); C(0;%s)$.''' % 
            (c1, c2, x_max, y_max, x_max, y_max, x_max, y_max, x_A, x_B, y_B, y_C, d1_y_start, x_max, d1_y_end, d2_y_start, x_max, d2_y_end, y_max, x_max, x_A, x_B, y_B, y_C, x_A, x_B, y_B, y_C))

            loigiai_vd_1_s = ('''Vẽ các đường thẳng và xác định miền nghiệm, ta thấy điểm $A$ nằm trên trục $Ox$ có tọa độ là nghiệm của $2x+y-%s=0$ khi $y=0$, suy ra $x=%s$. \\\\
            Vậy đỉnh $A(%s;0)$, khẳng định trên là sai.''' % (c2, x_A, x_A))

            loigiai_vd_1 = loigiai_vd_1_d if vd_da_1 == vd_da_1_d else loigiai_vd_1_s
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True $F(x,y)=%sx+%sy$ đạt giá trị lớn nhất là $%s$ tại $x = %s$ và $y = %s$' % (m, n, F_max, x_B, y_B)
            vdc_da_1_s = '$F(x,y)=%sx+%sy$ đạt giá trị lớn nhất là $%s$ tại $x = %s$ và $y = %s$' % (m, n, F_max+2, x_B, y_B)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1_d = ('''Ta tính giá trị của $F(x,y)=%sx+%sy$ tại các đỉnh của tứ giác $OABC$: \\\\
            $F(0;0) = 0$ \\\\
            $F(%s;0) = %s \\cdot %s + %s \\cdot 0 = %s$ \\\\
            $F(%s;%s) = %s \\cdot %s + %s \\cdot %s = %s$ \\\\
            $F(0;%s) = %s \\cdot 0 + %s \\cdot %s = %s$ \\\\
            Vậy $F(x,y)$ đạt giá trị lớn nhất là $%s$ tại $x = %s$ và $y = %s$.''' % (m, n, x_A, m, x_A, n, m*x_A, x_B, y_B, m, x_B, n, y_B, F_max, y_C, m, n, y_C, n*y_C, F_max, x_B, y_B))

            loigiai_vdc_1_s = loigiai_vdc_1_d + " Do đó khẳng định trên là sai."

            loigiai_vdc_1 = loigiai_vdc_1_d if vdc_da_1 == vdc_da_1_d else loigiai_vdc_1_s
            list_vdc_2 = [loigiai_vdc_1]

            ########################################################################
            # Trộn đáp án
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s
            loigiai_th_1 = loigiai_th_1_d if th_da_1 == th_da_1_d else loigiai_th_1_s
            loigiai_vd_1 = loigiai_vd_1_d if vd_da_1 == vd_da_1_d else loigiai_vd_1_s
            loigiai_vdc_1 = loigiai_vdc_1_d if vdc_da_1 == vdc_da_1_d else loigiai_vdc_1_s

            list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
            list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
            list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
            list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

