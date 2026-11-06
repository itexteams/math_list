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


def bt_dang33_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            k = symbols('k')

            # B3-Suy nghĩ tìm cách random bài toán
            list_goc = [Rational(1, 6), Rational(1, 4), Rational(1, 3)]
            goc_frac = random.choice(list_goc)

            goc_deg = int(goc_frac * 180)

            str_goc = latex(goc_frac) + '\\pi' if goc_frac != 1 else '\\pi'
            str_cung_lon = latex(2 - goc_frac) + '\\pi'
            str_cung_lon_sai = latex(1 + goc_frac) + '\\pi'

            # Nội dung câu hỏi và hình vẽ TikZ - ĐÃ XÓA CÁC DÒNG COMMENT BẮT ĐẦU BẰNG DẤU % ĐỂ TRÁNH LỖI PYTHON
            noidungcauhoi = ('''Cho hình vẽ sau:\\\\
            \\begin{center}
            \\begin{tikzpicture}[scale=1.8, line width=1pt, >=stealth]
                \\draw[->] (-1.4,0) -- (1.4,0) node[below] {$x$};
                \\draw[->] (0,-1.4) -- (0,1.4) node[left] {$y$};
                \\draw (0,0) circle (1);
                \\filldraw (0,0) circle (1pt) node[below right] {$O$};
                \\filldraw (1,0) circle (1pt) node[above right] {$A$};
                \\filldraw (0,1) circle (1pt) node[above right] {$B$};
                \\filldraw (-1,0) circle (1pt) node[above left] {$A'$};
                \\filldraw (0,-1) circle (1pt) node[below right] {$B'$};
                \\path (%s:1) coordinate (M);
                \\path (%s+180:1) coordinate (N);
                \\filldraw[red] (M) circle (1pt) node[above right, black] {$M$};
                \\filldraw[red] (N) circle (1pt) node[below left, black] {$N$};
                \\draw (N) -- (M);
                \\draw[fill=green!20, line width=0.6pt] (0,0) -- (0.25,0) arc (0:%s:0.25) -- cycle;
                \\node at (%s/2:0.45) {$\\frac{\\pi}{%s}$};
            \\end{tikzpicture}
            \\end{center}
            Xét tính đúng – sai của các phát biểu sau:''' 
                             % (str(goc_deg), str(goc_deg), str(goc_deg), str(goc_deg), latex(goc_frac.denominator)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_s = '$\\text{sđ}(OM,OA) = \\frac{\\pi}{%s} + k2\\pi$ ($k \\in \\mathbb{Z}$)' % (latex(goc_frac.denominator))
            nb_da_1_d = '\\True $\\text{sđ}(OA,OM) = \\frac{\\pi}{%s} + k2\\pi$ ($k \\in \\mathbb{Z}$)' % (latex(goc_frac.denominator))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Số đo của góc lượng giác $(OA,OM)$ có điểm đầu là tia $OA$ và điểm cuối là tia $OM$.\\\\
            Dựa vào hình vẽ, góc hình học $AOM$ bằng $\\frac{\\pi}{%s}$ và chiều từ $OA$ đến $OM$ là chiều dương.\\\\
            Do đó, $\\text{sđ}(OA,OM) = \\frac{\\pi}{%s} + k2\\pi$ ($k \\in \\mathbb{Z}$). Phát biểu lấy điểm đầu $OM$ là sai.''' 
                            % (latex(goc_frac.denominator), latex(goc_frac.denominator)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True $\\text{sđ}(ON,OA) = \\text{sđ}(ON,OM) - \\text{sđ}(OA,OM)$'
            th_da_1_s = '$\\text{sđ}(ON,OA) = \\text{sđ}(ON,OM) + \\text{sđ}(OA,OM)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Theo hệ thức Chasles đối với các tia lượng giác $OA, OM, ON$, ta có:\\\\
            $\\text{sđ}(OA,ON) = \\text{sđ}(OA,OM) + \\text{sđ}(OM,ON) + k2\\pi$\\\\
            Mặt khác, ta biết rằng $\\text{sđ}(ON,OA) = -\\text{sđ}(OA,ON) + k2\\pi$.\\\\
            Biến đổi hệ thức hiệu số đo giữa hai tia bất kỳ chung gốc: $\\text{sđ}(ON,OA) = \\text{sđ}(ON,OM) - \\text{sđ}(OA,OM)$. Đây là mệnh đề đúng.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Độ dài cung tròn $AM$ lớn là: $l_{AM} = \\frac{%s}{%s}\\pi$' % (latex((2 - goc_frac).numerator), latex((2 - goc_frac).denominator))
            vd_da_1_s = 'Độ dài cung tròn $AM$ lớn là: $l_{AM} = \\frac{%s}{%s}\\pi$' % (latex((1 + goc_frac).numerator), latex((1 + goc_frac).denominator))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Đường tròn lượng giác có bán kính $R = 1$.\\\\
            Cung nhỏ $AM$ tương ứng với góc ở tâm có số đo bằng $\\frac{\\pi}{%s}$.\\\\
            Do đó, cung lớn $AM$ tương ứng với góc ở tâm có số đo bằng $2\\pi - \\frac{\\pi}{%s} = \\frac{%s}{%s}\\pi$.\\\\
            Độ dài cung tròn $AM$ lớn là: $l = \\alpha \\cdot R = \\frac{%s}{%s}\\pi \\cdot 1 = \\frac{%s}{%s}\\pi$.''' 
                            % (latex(goc_frac.denominator), latex(goc_frac.denominator), latex((2 - goc_frac).numerator), latex((2 - goc_frac).denominator), latex((2 - goc_frac).numerator), latex((2 - goc_frac).denominator), latex((2 - goc_frac).numerator), latex((2 - goc_frac).denominator)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Hai điểm $M, N$ biểu diễn các cung có số đo là: $x = \\frac{\\pi}{%s} + k\\pi$ ($k \\in \\mathbb{Z}$)' % (latex(goc_frac.denominator))
            vdc_da_1_s = 'Hai điểm $M, N$ biểu diễn các cung có số đo là: $x = \\frac{\\pi}{%s} + k2\\pi$ ($k \\in \\mathbb{Z}$)' % (latex(goc_frac.denominator))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Điểm $M$ biểu diễn cho họ góc lượng giác $x = \\frac{\\pi}{%s} + k2\\pi$ ($k \\in \\mathbb{Z}$).\\\\
            Vì $M$ và $N$ đối xứng với nhau qua gốc tọa độ $O$, nên điểm $N$ biểu diễn cho họ góc lượng giác $x = \\frac{\\pi}{%s} + \\pi + k2\\pi$.\\\\
            Để gộp chung hai điểm đối xứng nhau qua gốc tọa độ $O$ trên đường tròn lượng giác, ta lấy số đo của một điểm cộng với chu kỳ là $k\\pi$.\\\\
            Vậy hai điểm $M, N$ biểu diễn chung cho các cung có số đo là: $x = \\frac{\\pi}{%s} + k\\pi$ ($k \\in \\mathbb{Z}$).''' 
                             % (latex(goc_frac.denominator), latex(goc_frac.denominator), latex(goc_frac.denominator)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

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

