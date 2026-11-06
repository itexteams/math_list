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


def bt_dang25_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random tham số
            # Phương trình đường thẳng d: ax + by = c (a,b,c > 0)
            a = randint(1, 4)
            b = randint(1, 4)
            while math.gcd(a, b) != 1: # Đảm bảo a, b nguyên tố cùng nhau để số đẹp hơn
                a = randint(1, 4)
                b = randint(1, 4)

            c = a * b

            # Tọa độ giao điểm
            x0 = c // a # Giao Ox (x0, 0)
            y0 = c // b # Giao Oy (0, y0)

            # Random bất phương trình ax + by < c (vì miền không gạch chứa gốc tọa độ, và biên là nét đứt)
            bt = a*x + b*y

            # Nội dung câu hỏi và hình vẽ
            tikz_code = ('''\\begin{tikzpicture}[>=stealth, scale=0.7]
            \\draw[->, thick] (-2,0) -- (%s,0) node[below] {$x$};
            \\draw[->, thick] (0,-2) -- (0,%s) node[right] {$y$};
            \\node at (-0.3,-0.3) {$O$};
            \\node at (%s,-0.3) {$%s$};
            \\node at (-0.3,%s) {$%s$};
            \\draw[dashed, thick] (-1, %s) node[left] {$d$} -- (%s, -1);
            \\fill[pattern=north east lines, pattern color=black] (-1, %s) -- (%s, -1) -- (%s, -1) -- (%s, %s) -- cycle;
            \\end{tikzpicture}'''
                % (x0 + 3, y0 + 3, x0, x0, y0, y0, (c + a)/b, (c + b)/a, (c + a)/b, (c + b)/a, x0 + 3, x0 + 3, y0 + 3)
            )

            noidungcauhoi = ('''Miền không bị gạch được cho bởi hình sau là miền nghiệm của một bất phương trình bậc nhất hai ẩn.
            \\begin{center}
            %s
            \\end{center}
            Các mệnh đề sau đúng hay sai?'''
                % (tikz_code)
            )

            ######################################################################## Nhận biết ############################################
            # Điểm O(0;0) thuộc miền không bị gạch
            nb_da_1_d = '\\True Điểm $O(0;0)$ thuộc miền không bị gạch'
            nb_da_1_s = 'Điểm $O(0;0)$ không thuộc miền không bị gạch'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            if '\\True' in nb_da_1:
                loigiai_nb_1 = ('''Quan sát hình vẽ ta thấy điểm $O(0;0)$ nằm trong miền không bị gạch. Do đó mệnh đề đúng.''')
            else:
                loigiai_nb_1 = ('''Quan sát hình vẽ ta thấy điểm $O(0;0)$ nằm trong miền không bị gạch. Do đó mệnh đề sai.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Phương trình đường thẳng d
            th_da_1_d = '\\True Đường thẳng $d$ có phương trình $%s = %s$' % (latex(bt), c)

            # Tạo 1 pt sai (đổi dấu hoặc đổi hệ số)
            bt_sai = b*x + a*y
            if bt == bt_sai: # Nếu a=b thì đổi dấu
                bt_sai = a*x - b*y
            th_da_1_s = 'Đường thẳng $d$ có phương trình $%s = %s$' % (latex(bt_sai), c)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            if '\\True' in th_da_1:
                loigiai_th_1 = ('''Đường thẳng $d$ đi qua hai điểm $(%s; 0)$ và $(0; %s)$ nên có phương trình theo đoạn chắn là: 
            $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow %s = %s$. Mệnh đề đúng.'''
                    % (x0, y0, x0, y0, latex(bt), c)
                )
            else:
                loigiai_th_1 = ('''Đường thẳng $d$ đi qua hai điểm $(%s; 0)$ và $(0; %s)$ nên có phương trình theo đoạn chắn là: 
            $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow %s = %s$. Phương trình ở mệnh đề không tương đương. Mệnh đề sai.'''
                    % (x0, y0, x0, y0, latex(bt), c)
                )

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Điểm O thuộc miền nghiệm BPT
            vd_da_1_d = '\\True Điểm $O(0;0)$ thuộc miền nghiệm của bất phương trình $%s < %s$' % (latex(bt), c)
            vd_da_1_s = 'Điểm $O(0;0)$ không thuộc miền nghiệm của bất phương trình $%s < %s$' % (latex(bt), c)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            if '\\True' in vd_da_1:
                loigiai_vd_1 = ('''Thay tọa độ $O(0;0)$ vào bất phương trình $%s < %s$ ta được: $0 < %s$ (đúng). \\\\
            Vậy $O(0;0)$ thuộc miền nghiệm của bất phương trình. Mệnh đề đúng.'''
                    % (latex(bt), c, c)
                )
            else:
                loigiai_vd_1 = ('''Thay tọa độ $O(0;0)$ vào bất phương trình $%s < %s$ ta được: $0 < %s$ (đúng). \\\\
            Vậy $O(0;0)$ thuộc miền nghiệm của bất phương trình. Mệnh đề sai.'''
                    % (latex(bt), c, c)
                )

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Miền không bị gạch là miền nghiệm
            vdc_da_1_d = '\\True Miền không bị gạch là miền nghiệm của bất phương trình $%s < %s$' % (latex(bt), c)
            vdc_da_1_s = 'Miền không bị gạch là miền nghiệm của bất phương trình $%s > %s$' % (latex(bt), c)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            if '\\True' in vdc_da_1:
                loigiai_vdc_1 = ('''Đường thẳng biên $d: %s = %s$ được vẽ bằng nét đứt nên miền nghiệm không chứa bờ $d$. \\\\
            Hơn nữa điểm $O(0;0)$ nằm trong miền không bị gạch và thỏa mãn $%s < %s$. \\\\
            Do đó miền không bị gạch là miền nghiệm của bất phương trình $%s < %s$. Mệnh đề đúng.'''
                    % (latex(bt), c, latex(bt), c, latex(bt), c)
                )
            else:
                loigiai_vdc_1 = ('''Đường thẳng biên $d: %s = %s$ được vẽ bằng nét đứt nên miền nghiệm không chứa bờ $d$. \\\\
            Hơn nữa điểm $O(0;0)$ nằm trong miền không bị gạch và thỏa mãn $0 < %s$ nên nó là miền nghiệm của $%s < %s$. \\\\
            Mệnh đề đã cho khẳng định là bất phương trình $%s > %s$. Do đó mệnh đề sai.'''
                    % (latex(bt), c, c, latex(bt), c, latex(bt), c)
                )

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (cập nhật lại lời giải tương ứng)
            list_nb_1 = [nb_da_1]
            if '\\True' in nb_da_1:
                list_nb_2 = [('''Quan sát hình vẽ ta thấy điểm $O(0;0)$ nằm trong miền không bị gạch. Do đó mệnh đề đúng.''')]
            else:
                list_nb_2 = [('''Quan sát hình vẽ ta thấy điểm $O(0;0)$ nằm trong miền không bị gạch. Do đó mệnh đề sai.''')]

            list_th_1 = [th_da_1]
            if '\\True' in th_da_1:
                list_th_2 = [('''Đường thẳng $d$ đi qua hai điểm $(%s; 0)$ và $(0; %s)$ nên có phương trình theo đoạn chắn là: 
            $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow %s = %s$. Mệnh đề đúng.'''
                    % (x0, y0, x0, y0, latex(bt), c))]
            else:
                list_th_2 = [('''Đường thẳng $d$ đi qua hai điểm $(%s; 0)$ và $(0; %s)$ nên có phương trình theo đoạn chắn là: 
            $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow %s = %s$. Phương trình ở mệnh đề không tương đương. Mệnh đề sai.'''
                    % (x0, y0, x0, y0, latex(bt), c))]

            list_vd_1 = [vd_da_1]
            if '\\True' in vd_da_1:
                list_vd_2 = [('''Thay tọa độ $O(0;0)$ vào bất phương trình $%s < %s$ ta được: $0 < %s$ (đúng). \\\\
            Vậy $O(0;0)$ thuộc miền nghiệm của bất phương trình. Mệnh đề đúng.'''
                    % (latex(bt), c, c))]
            else:
                list_vd_2 = [('''Thay tọa độ $O(0;0)$ vào bất phương trình $%s < %s$ ta được: $0 < %s$ (đúng). \\\\
            Vậy $O(0;0)$ thuộc miền nghiệm của bất phương trình. Mệnh đề sai.'''
                    % (latex(bt), c, c))]

            list_vdc_1 = [vdc_da_1]
            if '\\True' in vdc_da_1:
                list_vdc_2 = [('''Đường thẳng biên $d: %s = %s$ được vẽ bằng nét đứt nên miền nghiệm không chứa bờ $d$. \\\\
            Hơn nữa điểm $O(0;0)$ nằm trong miền không bị gạch và thỏa mãn $%s < %s$. \\\\
            Do đó miền không bị gạch là miền nghiệm của bất phương trình $%s < %s$. Mệnh đề đúng.'''
                    % (latex(bt), c, latex(bt), c, latex(bt), c))]
            else:
                list_vdc_2 = [('''Đường thẳng biên $d: %s = %s$ được vẽ bằng nét đứt nên miền nghiệm không chứa bờ $d$. \\\\
            Hơn nữa điểm $O(0;0)$ nằm trong miền không bị gạch và thỏa mãn $0 < %s$ nên nó là miền nghiệm của $%s < %s$. \\\\
            Mệnh đề đã cho khẳng định là bất phương trình $%s > %s$. Do đó mệnh đề sai.'''
                    % (latex(bt), c, c, latex(bt), c, latex(bt), c))]


            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

