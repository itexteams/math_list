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


def bt_dang5_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các hệ số cho ý b: h1*sin(alpha) + h2*cos(alpha) < 1
            h1 = randint(2, 4)
            h2 = randint(2, 4)

            # Vẽ hình bằng TikZ (độ dày nét 1pt, giữ đúng hình dạng mẫu)
            hinh_tikz = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=1.8, >=stealth]
              \\draw[->] (-1.4,0) -- (1.4,0) node[below] {$x$};
              \\draw[->] (0,-1.4) -- (0,1.4) node[left] {$y$};
              \\draw (0,0) circle (1);
              \\node[below left] at (0,0) {$O$};
              \\node[above right] at (1,0) {$A$};
              \\node[above right] at (0,1) {$B$};
              \\node[above left] at (-1,0) {$A'$};
              \\node[below right] at (0,-1) {$B'$};
              \\coordinate (M1) at (45:-1);
              \\coordinate (M2) at (45:1);
              \\coordinate (M3) at (135:1);
              \\coordinate (M4) at (135:-1);
              \\draw (M1) -- (M2) -- (M3) -- (M4) -- cycle;
              \\filldraw[fill=red] (M1) circle (1pt) node[left] {$M_1$};
              \\filldraw[fill=red] (M2) circle (1pt) node[right] {$M_2$};
              \\filldraw[fill=red] (M3) circle (1pt) node[left] {$M_3$};
              \\filldraw[fill=red] (M4) circle (1pt) node[right] {$M_4$};
            \\end{tikzpicture} \\end{center}''')

            # Nội dung câu hỏi sử dụng %s cho đề bài và chèn hình vẽ TikZ vào cuối
            noidungcauhoi = ('''Hình vẽ bên là vòng tròn lượng giác gốc $A$, trong đó $M_1M_2M_3M_4$ là hình vuông, $\\widehat{AOM_1} = 45^\\circ$. Xét góc lượng giác $\\alpha$ có điểm đầu là điểm $A$, điểm cuối là điểm bất kỳ nào đó trên vòng tròn lượng giác. %s'''
                             %(hinh_tikz))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Tại điểm cuối B thì sin(alpha) = 1
            nb_da_1_d = '\\True Tại điểm cuối $B$ thì $\\sin \\alpha = 1$'
            nb_da_1_s = 'Tại điểm cuối $B$ thì $\\sin \\alpha = 0$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Điểm $B(0;1)$ nằm trên trục tung tương ứng với góc lượng giác có điểm cuối trùng với $B$. Khi đó $\\sin \\alpha = y_B = 1$. Khẳng định này đúng.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Tại điểm cuối M3 thì h1*sin(alpha) + h2*cos(alpha) < 1
            # M3 có tọa độ x = -sqrt(2)/2, y = sqrt(2)/2. 
            # Biểu thức bằng: h1*(sqrt(2)/2) + h2*(-sqrt(2)/2) = (h1 - h2)*sqrt(2)/2
            val_m3 = (h1 - h2) * (math.sqrt(2)/2)
            if val_m3 < 1:
                th_da_1_d = '\\True Tại điểm cuối $M_3$ thì $%s\\sin \\alpha + %s\\cos \\alpha < 1$' %(latex(h1), latex(h2))
                th_da_1_s = 'Tại điểm cuối $M_3$ thì $%s\\sin \\alpha + %s\\cos \\alpha > 1$' %(latex(h1), latex(h2))
            else:
                th_da_1_d = '\\True Tại điểm cuối $M_3$ thì $%s\\sin \\alpha + %s\\cos \\alpha \\ge 1$' %(latex(h1), latex(h2))
                th_da_1_s = 'Tại điểm cuối $M_3$ thì $%s\\sin \\alpha + %s\\cos \\alpha < 1$' %(latex(h1), latex(h2))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            val_m3_str = str(round(val_m3, 2)).replace('.', ',')
            loigiai_th_1 = ('''Điểm $M_3$ nằm ở góc phần tư thứ II, tương ứng với cung $135^\\circ$. Do đó tọa độ của $M_3$ là $\\left(-\\frac{\\sqrt{2}}{2}; \\frac{\\sqrt{2}}{2}\\right)$. \\\\'''
                            '''Suy ra $\\sin \\alpha = \\frac{\\sqrt{2}}{2}$ và $\\cos \\alpha = -\\frac{\\sqrt{2}}{2}$. \\\\'''
                            '''Giá trị biểu thức là: $%s \\cdot \\frac{\\sqrt{2}}{2} + %s \\cdot \\left(-\\frac{\\sqrt{2}}{2}\\right) = \\frac{(%s - %s)\\sqrt{2}}{2} \\approx %s$. \\\\'''
                            '''So sánh giá trị này với $1$ để xác định tính đúng sai.'''
                            %(latex(h1), latex(h2), latex(h1), latex(h2), val_m3_str))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Hai điểm M2, M3 biểu diễn đầy đủ nghiệm của pt sin x = sqrt(2)/2
            vd_da_1_d = '\\True Hai điểm $M_2, M_3$ là điểm biểu diễn đầy đủ nghiệm của phương trình lượng giác $\\sin x = \\frac{\\sqrt{2}}{2}$'
            vd_da_1_s = 'Hai điểm $M_1, \\, M_2$ là điểm biểu diễn đầy đủ nghiệm của phương trình lượng giác $\\sin x = \\frac{\\sqrt{2}}{2}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Phương trình $\\sin x = \\frac{\\sqrt{2}}{2}$ có hai họ nghiệm trên một vòng tròn là $x = \\frac{\\pi}{4} + k2\\pi$ và $x = \\frac{3\\pi}{4} + k2\\pi$. \\\\'''
                            '''Trên đường tròn lượng giác, họ nghiệm thứ nhất được biểu diễn bởi điểm $M_2$ (góc $45^\\circ$) và họ nghiệm thứ hai được biểu diễn bởi điểm $M_3$ (góc $135^\\circ$). \\\\'''
                            '''Vậy hai điểm $M_2$ và $M_3$ biểu diễn đầy đủ nghiệm của phương trình.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Khi di chuyển từ M1 đến M2 thì tan(alpha) tăng dần
            vd_da_1_d = '\\True Khi di chuyển điểm cuối từ $M_1 \\rightarrow M_2$ thì $\\tan \\alpha$ tăng dần'
            vd_da_1_s = 'Khi di chuyển điểm cuối từ $M_1 \\rightarrow M_2$ thì $\\tan \\alpha$ giảm dần'
            list_vdc_da_1 = [vd_da_1_d, vd_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Điểm $M_1$ tương ứng góc $-45^\\circ$ và điểm $M_2$ tương ứng góc $45^\\circ$. \\\\'''
                             '''Khi di chuyển điểm cuối liên tục trên đường tròn theo chiều dương từ $M_1 \\rightarrow M_2$, góc $\\alpha$ tăng liên tục từ $-\\frac{\\pi}{4}$ đến $\\frac{\\pi}{4}$. \\\\'''
                             '''Trên khoảng $\\left(-\\frac{\\pi}{4}; \\frac{\\pi}{4}\\right)$, hàm số $y = \\tan \\alpha$ là hàm số đồng biến. \\\\'''
                             '''Do đó, khi điểm cuối di chuyển từ $M_1 \\rightarrow M_2$ thì giá trị $\\tan \\alpha$ luôn luôn tăng dần.''')

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra để đảm bảo số lượng đáp án đúng nằm trong khoảng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Thiết lập lại danh sách sau khi lọc thỏa mãn điều kiện
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

            # Xuất câu hỏi và lời giải chi tiết theo đúng định dạng mẫu khung chương trình đề ra
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

