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


def bt_dang4_p2_b2_c1_hh12(self):
    # Khai báo biến
    x0 = randint(100, 200)
    y0 = randint(250, 400)
    z0 = randint(8, 12)

    v1 = randint(700, 850)
    vw = random.choice([5, 10, 15, 20, 25])
    vw_kmh = int(vw * 3.6)
    v_total = v1 + vw_kmh

    y1 = y0 + v_total

    v2 = randint(350, 450) * 2
    d2 = int(v2 * 0.5)
    y2 = y1 - d2

    # Nội dung câu hỏi
    noidungcauhoi = ('''Hình vẽ sau mô tả vị trí của máy bay vào thời điểm 9h30 phút. Biết các đơn vị trên hình tính theo đơn vị km.
    \\begin{center}
    	\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    		\\draw[->, line width=1pt] (0,0) -- (-2.5,-1.5) node[below] {$x$ (Nam)};
    		\\draw[->, line width=1pt] (0,0) -- (4,0) node[below] {$y$ (Đông)};
    		\\draw[->, line width=1pt] (0,0) -- (0,3) node[left] {$z$};
    		\\node[below left] at (0,0) {$O$};
    		\\coordinate (X) at (-1.5,-0.9);
    		\\coordinate (Y) at (2.5,0);
    		\\coordinate (Z) at (0,2);
    		\\coordinate (XY) at (1,-0.9);
    		\\coordinate (M) at (1,1.1);
    		\\draw[dashed, line width=1pt] (X) -- (XY) -- (Y);
    		\\draw[dashed, line width=1pt] (XY) -- (M) -- (Z);
    		\\node[left] at (X) {$%s$};
    		\\node[above] at (Y) {$%s$};
    		\\node[left] at (Z) {$%s$};
    		\\begin{scope}[shift={(M)}, scale=0.1]
    			\\begin{scope}[shift={(-5.5,-3)}]
    				\\definecolor{outline}{RGB}{91,83,82}
    				\\definecolor{orangeLight}{RGB}{255,187,105}
    				\\definecolor{orangeDark}{RGB}{235,129,57}
    				\\definecolor{metal}{RGB}{193,190,193}
    				\\definecolor{glass}{RGB}{103,120,143}
    				\\tikzset{shell/.style={draw=outline,line width=.3pt,line join=round,line cap=round},seam/.style={draw=outline!75,line width=.2pt,line cap=round},panel/.style={shell,top color=orangeLight,bottom color=orangeDark,shading angle=25}
    				}
    				\\def\\engine{
    					\\path[panel] (0,.35).. controls (.33,.43) and (.83,.41).. (1.02,.24)
    					.. controls (1.08,.08) and (.97,-.15).. (.79,-.23)
    					.. controls (.51,-.36) and (.19,-.38).. (0,-.35) -- cycle;
    					\\fill[orangeLight] (.12,.29).. controls (.43,.37) and (.68,.31).. (.80,.19)
    					-- (.57,-.24) -- (.12,-.29) -- cycle;
    					\\filldraw[shell,fill=white] (0,0) ellipse ({.27} and .36);
    					\\filldraw[seam,fill=metal!65!outline] (-.02,0) ellipse (.20 and .28);
    					\\fill[outline!85] (-.05,0) ellipse ({.11} and .19);
    					\\fill[metal!65!outline] (-.06,.02) ellipse ({.06} and .12);
    				}
    				\\newcommand{\\fuselagepath}{(Nose)
    					.. controls (.04,1.19) and (.75,2.16).. (1.50,2.57)
    					.. controls (3.12,3.51) and (6.03,4.43).. (Tail)
    					.. controls (8.61,5.12) and (8.96,4.72).. (8.77,4.06)
    					.. controls (8.68,3.62) and (7.61,2.99).. (6.66,2.57)
    					.. controls (4.37,1.54) and (1.86,.12).. (.83,.22)
    					.. controls (.23,.24) and (-.08,.39).. (Nose) -- cycle
    				}
    				\\coordinate (Nose) at (.02,.73);
    				\\coordinate (Tail) at (8.18,5.10);
    				\\coordinate (FarTip) at (.42,5.65);
    				\\coordinate (NearTip) at (10.50,.05);
    				\\coordinate (FarEngine) at (2.22,3.05);
    				\\coordinate (NearEngine) at (6.68,.47);
    				\\coordinate (WindowStart) at (3.62,1.94);
    				\\filldraw[shell,fill=white] (8.55,5.23) -- (7.76,5.91)
    				.. controls (7.58,6.05) and (7.86,6.15).. (8.05,6.22)
    				-- (9.16,5.78) -- cycle;
    				\\path[panel] (8.62,5.43) -- (7.95,6.02) -- (8.08,6.09)
    				-- (8.94,5.75) -- cycle;
    				\\path[panel] (.78,5.89).. controls (.95,6.11) and (1.19,6.29).. (1.35,6.33)
    				-- (1.20,5.95) -- cycle;
    				\\foreach \\i in {0,1}{
    					\\begin{scope}[shift={({.55*\\i},{-.3575*\\i})}]
    						\\filldraw[shell,fill=metal] (1.69,4.48) -- (1.22,4.17)
    						.. controls (1.00,3.97) and (1.26,3.91).. (1.49,4.04)
    						-- (2.07,4.29) -- cycle;
    					\\end{scope}
    				}
    				\\begin{scope}[shift={(FarEngine)},rotate=20,scale=.85]
    					\\engine
    				\\end{scope}
    				\\filldraw[shell,fill=white] (2.34,3.39) -- (2.56,3.49) -- (2.76,3.42)
    				-- (2.52,3.32) -- cycle;
    				\\filldraw[shell,fill=white] (5.19,3.96) -- (1.30,5.93)
    				.. controls (1.20,6.00) and (.83,5.86).. (FarTip)
    				.. controls (.20,5.53) and (.48,5.36).. (.61,5.24)
    				-- (3.08,3.28) -- cycle;
    				\\path[panel] (4.91,4.00) -- (1.24,5.80) -- (.65,5.64)
    				-- (3.39,3.51) -- cycle;
    				\\fill[orangeDark] (3.39,3.51) -- (4.91,4.00) -- (4.72,4.10)
    				-- (3.24,3.63) -- cycle;
    				\\path[panel] (7.99,4.86) -- (9.72,5.55)
    				.. controls (10.23,5.79) and (10.14,5.26).. (9.73,4.90)
    				-- (8.70,3.83) -- (8.11,4.06) -- cycle;
    				\\fill[orangeLight] (8.20,4.82) -- (9.67,5.35) -- (9.15,4.68)
    				-- (8.61,4.11) -- cycle;
    				\\filldraw[shell,fill=white] (8.18,5.10)
    				.. controls (8.51,5.13) and (8.57,5.35).. (8.76,5.67)
    				-- (9.53,7.10)
    				.. controls (9.61,7.25) and (10.25,7.47).. (10.30,7.35)
    				-- (9.87,5.52)
    				.. controls (9.58,5.28) and (8.68,4.99).. (8.18,5.10) -- cycle;
    				\\path[panel] (8.48,5.06)
    				.. controls (8.70,5.19) and (8.76,5.40).. (8.95,5.73)
    				-- (9.67,7.00)
    				.. controls (9.76,7.12) and (10.04,7.21).. (10.24,7.29)
    				-- (9.83,5.57)
    				.. controls (9.49,5.34) and (8.89,5.18).. (8.48,5.06) -- cycle;
    				\\fill[orangeDark,opacity=.55] (8.48,5.06)
    				.. controls (9.14,5.39) and (9.36,5.46).. (9.49,5.75)
    				-- (10.24,7.29) -- (9.83,5.57)
    				.. controls (9.49,5.34) and (8.89,5.18).. (8.48,5.06) -- cycle;
    				\\filldraw[shell,fill=white] (9.25,4.84)
    				.. controls (9.22,4.94) and (9.71,5.27).. (9.97,5.33)
    				-- (11.36,4.79)
    				.. controls (11.63,4.67) and (11.35,4.51).. (11.07,4.43) -- cycle;
    				\\path[panel] (9.43,4.98) -- (9.98,5.20) -- (11.20,4.72)
    				-- (11.03,4.59) -- cycle;
    				\\draw[seam] (9.25,4.84) -- (11.07,4.43);
    				\\path[fill=white] \\fuselagepath;
    				\\begin{scope}
    					\\clip \\fuselagepath;
    					\\fill[metal] (-.10,.75)
    					.. controls (.87,.11) and (3.26,1.31).. (5.67,2.48)
    					.. controls (7.53,3.40) and (8.47,4.13).. (9.12,4.71)
    					-- (9.22,3.29) -- (1.23,-.27) -- (-.17,.04) -- cycle;
    					\\fill[white!45!metal] (-.08,.71)
    					.. controls (1.09,.11) and (3.28,1.57).. (5.72,2.75)
    					.. controls (7.63,3.68) and (8.42,4.14).. (9.08,4.72)
    					-- (8.83,4.20)
    					.. controls (7.37,3.08) and (3.08,1.08).. (.72,.34)
    					-- (-.09,.46) -- cycle;
    					\\fill[glass!2!white] (.77,1.76)
    					.. controls (1.15,2.40) and (5.73,4.12).. (8.29,4.94)
    					-- (8.07,5.31) -- (1.15,2.74) -- cycle;
    				\\end{scope}
    				\\draw[shell] \\fuselagepath;
    				\\draw[seam] (8.45,4.58).. controls (8.64,4.32) and (8.58,3.98).. (8.43,3.73);
    				\\draw[seam] (1.08,1.17).. controls (1.33,.99) and (1.43,.76).. (1.29,.56);
    				\\foreach \\i in {0,...,11}{
    					\\coordinate (Window) at ($(WindowStart)+(.50*\\i-.008*\\i*\\i,.235*\\i-.003*\\i*\\i)$);
    					\\pgfmathsetmacro{\\ww}{.28-.009*\\i}
    					\\pgfmathsetmacro{\\wh}{.34-.007*\\i}
    					\\begin{scope}[shift={(Window)},rotate=17]
    						\\filldraw[draw=glass!65!metal,fill=glass!70!metal,line width=.15pt,rounded corners=1pt] (-.5*\\ww,-.5*\\wh) rectangle (.5*\\ww,.5*\\wh);
    					\\end{scope}
    				}
    				\\filldraw[shell,fill=white,rounded corners=1pt] (2.95,.99) -- (3.26,1.14)
    				.. controls (3.35,1.41) and (3.28,1.93).. (3.16,2.15)
    				-- (2.89,2.04)
    				.. controls (3.00,1.66) and (3.06,1.26).. (2.95,.99) -- cycle;
    				\\fill[outline!80] (3.14,1.62) ellipse (.04 and .06);
    				\\filldraw[shell,fill=glass] (.59,1.67) -- (.74,1.92) -- (.97,2.11)
    				-- (1.02,1.96) -- (.68,1.46) -- cycle;
    				\\filldraw[shell,fill=glass] (.77,1.45) -- (1.10,1.89)
    				.. controls (1.26,1.79) and (1.47,1.76).. (1.66,1.74)
    				-- (1.55,1.24)
    				.. controls (1.26,1.22) and (1.02,1.32).. (.77,1.45) -- cycle;
    				\\filldraw[shell,fill=glass] (1.72,1.26) -- (1.79,1.72) -- (2.22,1.77)
    				.. controls (2.31,1.70) and (2.36,1.48).. (2.29,1.39)
    				-- cycle;
    				\\filldraw[shell,fill=metal] (4.35,1.35)
    				.. controls (4.30,1.52) and (4.66,1.97).. (4.97,2.17)
    				-- (6.65,2.90) -- (7.33,2.63) -- (5.47,1.55) -- cycle;
    				\\filldraw[shell,fill=metal] (8.54,.58) -- (7.98,.23)
    				.. controls (7.74,.08) and (7.95,-.04).. (8.19,.13)
    				-- (8.96,.51) -- cycle;
    				\\begin{scope}[shift={(NearEngine)},rotate=20]
    					\\engine
    				\\end{scope}
    				\\filldraw[shell,fill=white] (6.70,.91) -- (6.89,1.15) -- (7.35,1.14)
    				-- (7.08,.87) -- (6.88,.82) -- cycle;
    				\\filldraw[shell,fill=white] (4.92,2.12)
    				.. controls (5.24,2.47) and (6.42,2.87).. (6.82,2.97)
    				.. controls (6.98,3.02) and (7.11,2.99).. (7.30,2.87)
    				-- (11.21,.78) -- (11.43,.64)
    				.. controls (11.40,.43) and (10.90,.02).. (NearTip)
    				.. controls (10.12,.02) and (6.32,1.19).. (4.76,1.61)
    				.. controls (4.61,1.68) and (4.77,1.97).. (4.92,2.12) -- cycle;
    				\\path[panel] (4.92,2.12)
    				.. controls (5.25,2.43) and (6.42,2.81).. (6.80,2.88)
    				-- (10.98,.68) -- (10.50,.37) -- cycle;
    				\\fill[orangeDark,opacity=.55] (4.92,2.12)
    				.. controls (5.25,2.43) and (6.42,2.81).. (6.80,2.88)
    				-- (7.20,2.67)
    				.. controls (6.60,2.72) and (5.36,2.42).. (5.12,2.05) -- cycle;
    				\\draw[shell] (4.92,2.12) -- (10.50,.37);
    				\\draw[seam] (10.50,.37).. controls (10.35,.23) and (10.25,.08).. (10.43,.05);
    				\\path[panel] (11.00,.43)
    				.. controls (11.22,.80) and (11.47,1.00).. (11.68,1.12)
    				.. controls (11.57,.79) and (11.32,.51).. (11.00,.43) -- cycle;
    			\\end{scope}
    		\\end{scope}
    	\\end{tikzpicture}
    \\end{center}'''
                     %(latex(x0),latex(y0),latex(z0)
                         ))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Máy bay đang ở độ cao $%s$ km' % (latex(z0))
    nb_da_1_s = 'Máy bay đang ở độ cao $%s$ km' % (latex(z0 + randint(1, 5)))
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Dựa vào hình vẽ, hình chiếu của máy bay lên trục $Oz$ là $%s$ nên máy bay đang ở độ cao $%s$ km.'''
                %(latex(z0), latex(z0))
                )

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Tọa độ của máy bay $(%s; %s; %s)$' % (latex(x0), latex(y0), latex(z0))
    th_da_1_s = 'Tọa độ của máy bay $(%s; %s; %s)$' % (latex(y0), latex(x0), latex(z0))
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Hình chiếu của máy bay lên trục $Ox$ là $%s$, lên trục $Oy$ là $%s$, lên trục $Oz$ là $%s$. Do đó tọa độ máy bay là $(%s; %s; %s)$.'''
               %(latex(x0), latex(y0), latex(z0), latex(x0), latex(y0), latex(z0))
               )

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Phi công để máy bay ở chế độ tự động với vận tốc theo hướng đông là $%s$ km/h, độ cao không đổi. Biết rằng gió thổi theo hướng đông với vận tốc $%s$ m/s. Giả sử vận tốc và hướng gió không đổi thì lúc 10h30 phút máy bay ở tọa độ $(%s; %s; %s)$' % (latex(v1), latex(vw), latex(x0), latex(y1), latex(z0))
    vd_da_1_s = 'Phi công để máy bay ở chế độ tự động với vận tốc theo hướng đông là $%s$ km/h, độ cao không đổi. Biết rằng gió thổi theo hướng đông với vận tốc $%s$ m/s. Giả sử vận tốc và hướng gió không đổi thì lúc 10h30 phút máy bay ở tọa độ $(%s; %s; %s)$' % (latex(v1), latex(vw), latex(x0), latex(y1 + randint(10, 50)), latex(z0))
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Thời gian bay từ 9h30 phút đến 10h30 phút là $t = 1$ giờ.\\\\
    Vận tốc của gió là $v_{\\text{gió}} = %s \\text{ m/s} = %s \\text{ km/h}$.\\\\
    Vận tốc thực tế của máy bay theo hướng đông (cùng hướng gió) là $v = %s + %s = %s \\text{ km/h}$.\\\\
    Quãng đường máy bay bay được trong $1$ giờ là $s = v \\cdot t = %s \\cdot 1 = %s \\text{ km}$.\\\\
    Vì máy bay bay theo hướng đông (cùng chiều dương trục $Oy$), tọa độ mới trên trục $Oy$ của máy bay là $y = %s + %s = %s$.\\\\
    Vậy lúc 10h30 phút, máy bay ở tọa độ $(%s; %s; %s)$.'''
               %(latex(vw), latex(vw_kmh), latex(v1), latex(vw_kmh), latex(v_total), latex(v_total), latex(v_total), latex(y0), latex(v_total), latex(y1), latex(x0), latex(y1), latex(z0))
               )

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Sau khi bay đến vị trí lúc 10h30 thì máy bay bay theo hướng ngược lại với vận tốc $%s$ km/h với độ cao không đổi, biết lúc đó trời lặng gió thì lúc 11h máy bay ở tọa độ $(%s; %s; %s)$' % (latex(v2), latex(x0), latex(y2), latex(z0))
    vdc_da_1_s = 'Sau khi bay đến vị trí lúc 10h30 thì máy bay bay theo hướng ngược lại với vận tốc $%s$ km/h với độ cao không đổi, biết lúc đó trời lặng gió thì lúc 11h máy bay ở tọa độ $(%s; %s; %s)$' % (latex(v2), latex(y2), latex(x0), latex(z0))
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Thời gian bay từ 10h30 đến 11h là $t' = 0,5$ giờ.\\\\
    Quãng đường máy bay bay được là $s' = %s \\cdot 0,5 = %s \\text{ km}$.\\\\
    Vì máy bay bay theo hướng ngược lại (hướng tây, ngược chiều dương trục $Oy$), tọa độ mới trên trục $Oy$ là $y' = %s - %s = %s$.\\\\
    Vậy lúc 11h máy bay ở tọa độ $(%s; %s; %s)$.'''
               %(latex(v2), latex(d2), latex(y1), latex(d2), latex(y2), latex(x0), latex(y2), latex(z0))
               )

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

